# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
# from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player

def player(prev_play, opponent_history=[],order=[{
    "RR": 0,
    "RP": 0,
    "RS": 0,
    "PR": 0,
    "PP": 0,
    "PS": 0,
    "SR": 0,
    "SP": 0,
    "SS": 0,
}]):
    if prev_play == '':
        prev_play = 'R'
    opponent_history.append(prev_play)
    right_move = {'P': 'S', 'R': 'P', 'S': 'R'}
    preds = []
    
    if len(opponent_history) > 2:
    # extract last two values 
        last_pair = ''.join(opponent_history[-2:])
        order[0][last_pair] += 1
        possibility = {
            prev_play + "R" : 0,
            prev_play + "S" : 0 ,
            prev_play + "P" : 0 ,}

        for p in possibility:
            if p in order[0]:
                possibility[p] = order[0][p]
        pred = max(possibility,key=possibility.get)
        preds.append(pred[-1])
        return right_move[pred[-1]]




    
    

    # return guess