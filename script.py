import random

inp = Element("inp")
res = Element("result")


def play_game(*args):
    user_guess = inp.value
    machine_guess = random.randint(1, 5)
    
    if int(user_guess) == machine_guess:
        res.element.classList.replace("text-gray-500", "text-blue-500")
        res.element.classList.replace("text-rose-600", "text-blue-500")
        res.element.innerText = "You Win!"
        
    else:
        res.element.classList.replace("text-gray-500", "text-rose-600")
        res.element.classList.replace("text-blue-500", "text-rose-600")
        res.element.innerText = f"Game Lost!, Code is {machine_guess}"
