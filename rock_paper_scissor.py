import random
user_score = 0
bot_score = 0
no_of_games = 3

print('Welcome, number of games would be 3')

while no_of_games>0:
    print('Give input- Rock/Paper/Scissor or q for quitting the game')
    user_input = input('').lower()
    bot_input = random.randint(1,4) # 1 means bot choose Rock, 2- Paper, 3-Scissor
    if user_input == 'q':
        quit()
    if user_input == 'rock' and bot_input == 1:
        print(f'Draw! Bot choose rock. Give next input')
    if user_input == 'paper' and bot_input == 2:
            print(f'Draw! Bot choose paper. Give next input')
    if user_input == 'scissor' and bot_input == 3:
            print(f'Draw! Bot choose scissor. Give next input')
    if user_input == 'rock' and bot_input == 2:
            print(f'You lose. Bot choose paper. Give next input')
            bot_score += 1
    if user_input == 'rock' and bot_input == 3:
                print(f'You won. Bot choose scissor. Give next input')
                user_score += 1
    if user_input == 'paper' and bot_input == 1:
                print(f'You won. Bot choose rock. Give next input')
                user_score += 1
    if user_input == 'paper' and bot_input == 3:
                print(f'You lose. Bot choose scissor. Give next input')
                bot_score += 1
    if user_input == 'scissor' and bot_input == 1:
                print(f'You lose. Bot choose rock. Give next input')
                bot_score += 1
    if user_input == 'scissor' and bot_input == 2:
                print(f'You won. Bot choose paper. Give next input')
                user_score += 1
    no_of_games -= 1
print(f'Your final score- {user_score}, bot_score {bot_score}')