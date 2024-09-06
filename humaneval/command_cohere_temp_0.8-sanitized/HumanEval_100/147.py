def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]

    # Iterate through odd and even levels, updating pile size accordingly
    for i in range(1, n.bit_length() + 2):
        if i & 1:  # If level is odd, use next odd number
            pile.append(pile[-1] + 2)
        else:     # Otherwise, use next even number
            pile.append(pile[-1] + 1)

    return pile