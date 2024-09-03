def compare(game, guess):
    scores = game
    result = [0] * len(game)
    for i in range(len(game)):
        result[i] = abs(scores[i] - guess[i])
    return result