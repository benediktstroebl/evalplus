def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]

    # Loop to construct the pile incrementally
    for i in range(1, n // 2 + 1):
        pile.append(pile[i - 1] + 2 - (i % 2))

    # If the pile has an odd number of levels, append the last even pile size
    if n % 2 != 0:
        pile.append(pile[-1] + 2)

    return pile