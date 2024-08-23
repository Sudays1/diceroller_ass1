from pyscript import document
from dice import dice_roll

dice_type = "coin"
dice_num = 1

def select_face_option(event):
    global dice_type
    dice_type = document.getElementById('dice-type').value

def update_dice_num(event):
    global dice_num
    dice_num = int(document.getElementById('dice-num').value)

def roll_all_dice(event):
    global dice_type, dice_num

    update_dice_num(event)

    results = ""
    for _ in range(dice_num):
        result = dice_roll(dice_type)
        results += f"Rolling a {dice_type}: {result}\n"

    history_div = document.querySelector("div#roll-history")
    history_div.textContent = results

def clear_history(event):
    document.querySelector("div#roll-history").innerHTML = ""


