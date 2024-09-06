def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]

    # Loop to construct the pile by adding odd or even numbers
    while len(pile) < n + 1:
        if pile[-1] % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)

    return pile