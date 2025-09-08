import random 



def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
    sum_of_rolls = sum(rolls)
    return rolls, sum_of_rolls

def main():
    while True:
        try: 
            user_input: str = input('How many dice would you like to roll? ')

            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            # print(*roll_dice(int(user_input)), sep=', ')
            dice_roll = roll_dice(int(user_input))
            print(*dice_roll[0], sep=', ', end=" ") 
            print(f'({dice_roll[1]})')
        except ValueError:
            print('(Please enter a valid number!!)')


if __name__ == '__main__':
    main()
