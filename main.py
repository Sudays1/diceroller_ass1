from pyscript import document
from dice import dice_roll

dice_type = "coin"

def dice_num():






def select_face_option(event):
    global dice_type
    dice_type = document.getElementById('dice-type').value

def roll_all_dice(event):
    global dice_type

    for r in ...:
       results = dice_roll(dice_type)

def clear_history(event):
    document.querySelector("div#roll-history").innerHTML = ""



