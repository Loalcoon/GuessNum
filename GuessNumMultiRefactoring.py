import random

num = random.randint(1, 100)
player_1 = input('Enter the name of first player: ')
player_2 = input('Enter the name of second player: ')
player1_count = 0
player2_count = 0

max_difficulty = {'Easy': 9999, 'Medium': 10, 'Hard': 3}

def choose_difficulty():
    while True:
        user_difficulty = input('Choose Difficulty: Easy/Medium/Hard: ').capitalize()
        if user_difficulty in max_difficulty:
            return max_difficulty[user_difficulty]
        print("Invalid input. Please choose: Easy, Medium, or Hard.")

max_attempts = choose_difficulty()
print('Max attempts based on difficulty: ', max_attempts)


# Выбор сложности

current_player = random.randint(1, 2)
if current_player == 1:
    print(f'First to play is: {player_1}')
else:
    print(f'First to play is: {player_2}')


def get_player_input():
    while True:
        guess = input('Enter the number from 1 to 100 or `q` to exit: ')
        if guess.lower() == 'q':
            return None
        try:
            return int(guess)
        except ValueError:
            print('Enter a valid number!')

#Запуск игры

def process_guess(guess, num):
    if guess > num:
        return 'Too hot, guess lower'
    elif guess < num:
        return 'Too cold, guess higher'
    elif guess == num:
        return 'Correct'
# Логика

def switch_player(current_player, player1_count, player2_count):
    if current_player == 1:
        player1_count +=1
        return 2, player1_count, player2_count
    else:
        player2_count += 1
        return 1, player1_count, player2_count

# Выбор хода

def attempt_loss(player1_count, player2_count, max_attempts, player_1, player_2):
    if player1_count >= max_attempts:
        print(f'{player_1} is out of attempts. {player_2} Wins!')
        return True
    elif player2_count >= max_attempts:
        print(f'{player_2} is out of attempts. {player_1} Wins!')
        return True
    return False
# Проверка на количество ходов

while True:
    guess = get_player_input()

    if guess is None:
        if current_player == 1:
            print(f'{player_1} exited the game.')
        else:
            print(f'{player_2} exited the game.')
        break
    result = process_guess(guess, num)
    if result == "Correct":
        if current_player == 1:
            print(f"{player_1} won the game in {player1_count} attempts! Guess number was: {num}")
        else:
            print(f"{player_2} won the game in {player2_count} attempts! Guess number was: {num}")
        break

    current_player, player1_count, player2_count = switch_player(current_player, player1_count, player2_count)

    if current_player == 1:
        print(f"It's {player_1}'s turn! {player_2} has {max_attempts - player2_count} guesses left")
    else:
        print(f"It's {player_2}'s turn! {player_1} has {max_attempts - player1_count} guesses left")

    if attempt_loss(player1_count, player2_count, max_attempts, player_1, player_2):
        break
