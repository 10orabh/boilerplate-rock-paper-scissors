import random

def player(prev_play, opponent_history=[], order={}):
    if prev_play == "":
        prev_play = "R"

    opponent_history.append(prev_play)

    
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    
    last_three = "".join(opponent_history[-3:])
    if last_three not in order:
        order[last_three] = {"R": 0, "P": 0, "S": 0}

    
    if len(opponent_history) > 3:
        prev_seq = "".join(opponent_history[-4:-1])
        next_move = opponent_history[-1]
        if prev_seq not in order:
            order[prev_seq] = {"R": 0, "P": 0, "S": 0}
        order[prev_seq][next_move] += 1

    
    options = order.get(last_three, {"R": 0, "P": 0, "S": 0})
    predicted = max(options, key=options.get)

    
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[predicted]
