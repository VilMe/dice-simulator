import random 



def roll_dice(amount: int = 2) => list[int]:
    if amount <= 0;
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

