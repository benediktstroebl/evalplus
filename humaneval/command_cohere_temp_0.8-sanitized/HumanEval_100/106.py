def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]

    # Loop through each level (starting from the second level)
    for i in range(1, n.bit_length() + 1):
        # Check if the current level is odd or even
        if i % 2 == n % 2:
            pile.append(pile[i - 1])
        else:
            # If the current level is even and the previous level is odd,
            # we need to skip one even number
            if i % 2 == 0 and n % 2 == 1:
                pile.append(pile[i - 1] + 2)
            else:
                pile.append(pile[i - 1] + 1)

    return pile