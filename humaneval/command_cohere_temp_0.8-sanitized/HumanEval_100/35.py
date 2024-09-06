def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]

    # Loop through odd levels, incrementing the pile size by 2
    while pile[-1] % 2 == 1:
        pile.append(pile[-1] + 2)

    # Loop through even levels, incrementing the pile size by 1
    while pile[-1] % 2 == 0:
        pile.append(pile[-1] + 1)

    return pile