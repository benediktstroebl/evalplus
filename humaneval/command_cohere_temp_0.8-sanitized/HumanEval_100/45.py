def make_a_pile(n):
    # Calculate the first two levels directly
    pile = [n, n + 2]
    while len(pile) < n:
        # If the top of the pile is even, take an even number
        if pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        # Otherwise, take an odd number
        else:
            pile.append(pile[-1] + 1)
    return pile