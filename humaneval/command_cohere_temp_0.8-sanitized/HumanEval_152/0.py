def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
game = [1,2,3,4,5,1]
guess = [1,2,3,4,2,-2]