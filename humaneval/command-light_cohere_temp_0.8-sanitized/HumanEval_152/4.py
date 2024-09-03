def compare(game, guess):
    scores = game
    n = len(scores)
    result = [0] * n

    # Initialize all score differences to positive values.
    for i in range(n):
        result[i] = scores[i]

    for i in range(n):
        if guess[i] == scores[i]:
            result[i] = 0

    # Calculate the differences between guess and scores
    for i in range(n):
        result[i] = abs(guess[i] - scores[i])

    return result