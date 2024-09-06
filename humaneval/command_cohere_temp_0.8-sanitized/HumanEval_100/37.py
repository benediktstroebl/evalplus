def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]

    # Loop through and calculate the number of stones for each level based on the given rules
    for l in range(1, n + 1):
        if l % 2 == 0 and pile[l % 2 - 1] % 2 == 1:
            pile.append(pile[l % 2 - 1] + 1)
        elif l % 2 != 0 and pile[l % 2 - 1] % 2 == 0:
            pile.append(pile[l % 2 - 1] + 2)

    return pile