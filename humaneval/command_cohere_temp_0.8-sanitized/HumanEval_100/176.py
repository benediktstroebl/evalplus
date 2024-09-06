def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]

    # Loop to create subsequent levels
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:
            pile.append(i * 3 - 1)
        else:
            pile.append(i * 2)

    # Return the pile of stones
    return pile