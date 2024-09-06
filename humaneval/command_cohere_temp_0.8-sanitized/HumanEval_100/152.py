def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]

    # Loop to build the pile incrementally
    for i in range(1, n):
        if i % 2 == 1:
            pile.append(i + 2)
        else:
            pile.append(i + 1)

    return pile