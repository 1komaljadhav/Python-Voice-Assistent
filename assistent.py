import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes  # pip install pyjokes
import psutil  # pip install psutil
import pyautogui  # pip install pyautogui
from googlesearch import search  # pip install google
import random
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def tellJoke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


def systemInfo():
    cpu_usage = psutil.cpu_percent()
    battery = psutil.sensors_battery()
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Battery: {battery.percent}%")
    speak(f"CPU Usage is {cpu_usage} percent. Battery is {battery.percent} percent.")


def takeScreenshot():
    screenshot_path = "screenshot.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    print(f"Screenshot saved as {screenshot_path}")
    speak("Screenshot taken and saved.")


def googleSearch(query):
    speak(f"Searching Google for {query}")
    for j in search(query, num=1, stop=1, pause=2):
        print(j)
        webbrowser.open(j)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def playGame():
    games = [ "Tic Tac Toe", "Rock Paper Scissors"]
    selected_game = random.choice(games)
    print(f"Let's play {selected_game}!")
    speak(f"Let's play {selected_game}!")

    if selected_game == "Chess":
        playChess()
    elif selected_game == "Tic Tac Toe":
        playTicTacToe()
    elif selected_game == "Rock Paper Scissors":
        playRockPaperScissors()

def playTicTacToe():
    board = [" " for _ in range(9)]
    current_player = "X"

    def print_board():
        for i in range(0, 9, 3):
            print(" | ".join(board[i:i + 3]))
            if i < 6:
                print("---------")

    def is_winner():
        # Check rows, columns, and diagonals
        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] != " ":
                return True
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != " ":
                return True
        if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
            return True
        return False

    def is_board_full():
        return " " not in board

    def take_turn():
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if 0 <= move < 9 and board[move] == " ":
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
        print_board()
        move = take_turn()
        board[move] = current_player

        if is_winner():
            print_board()
            print(f"Player {current_player} wins!")
            speak(f"Player {current_player} wins!")
            break
        elif is_board_full():
            print_board()
            print("It's a draw!")
            speak("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

def playRockPaperScissors():
    choices = ["rock", "paper", "scissors"]
    player_choice = takeCommand().lower()

    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        speak("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"Player chooses {player_choice}")
    print(f"Computer chooses {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
        speak("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("Player wins!")
        speak("Player wins!")
    else:
        print("Computer wins!")
        speak("Computer wins!")


def openWebsite():
    speak("Sure, which website would you like to open?")
    website_name = takeCommand().lower()
    webbrowser.open(f"https://www.{website_name}.com")


def calculate(expression):
    try:
        result = eval(expression)
        print(f"Result: {result}")
        speak(f"The result is {result}")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't calculate that.")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")

        elif 'tell me a joke' in query:
            tellJoke()

        elif 'system information' in query:
            systemInfo()

        elif 'take a screenshot' in query:
            takeScreenshot()

        elif 'search on google' in query:
            # Example: "search on google Python programming"
            search_query = query.replace("search on google", "")
            googleSearch(search_query)

        elif 'play a game' in query:
            playGame()

        elif 'open website' in query:
            openWebsite()

        elif 'calculate' in query:
            # Example: "calculate 2 + 2"
            expression = query.replace("calculate", "").strip()
            calculate(expression)
