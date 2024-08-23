import random

def dice_roll(dice_type):
    if dice_type == 'coin':
        return random.randint(1, 2)
    elif dice_type == 'd4':
        return random.randint(1, 4)
    elif dice_type == 'd6':
        return random.randint(1, 6)
    elif dice_type == 'd8':
        return random.randint(1, 8)
    elif dice_type == 'd10':
        return random.randint(1, 10)
    elif dice_type == 'd20':
        return random.randint(1, 20)
    elif dice_type == 'd100':
        return random.randint(1, 100)
    else:
        raise ValueError("Invalid dice type. Choose from 'coin', 'd4', 'd6', 'd8', 'd10', 'd20', 'd100'.")


