def compare(game, guess):
    """
    Your task description here.
    Returns an array of matches, which is [0,0,0,0,...], or [number, number, number, ...].
    """
    matches = [0] * len(game)
    for i in range(len(game)):
        if game[i] == guess[i]:
            matches[i] = 1
    return matches