def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game,guess)]