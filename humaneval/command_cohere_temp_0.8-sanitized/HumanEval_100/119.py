def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]

    # Loop through and calculate the number of stones for each level based on the given rules
    for i in range(1, n.bit_length() + 1):
        if n & (1 << i) != 0:  # If the current bit is set to 1, it's odd, so multiply by 3
            pile.append(pile[-1] * 3)
        else:  # else it's even, so multiply by 2
            pile.append(pile[-1] * 2)

    return pile