def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]

    # Loop to create additional levels according to the problem specification
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:  # If the current level is odd (first or third, etc.)
            pile.append(i + 2)
        else:  # If the current level is even (second or fourth, etc.)
            pile.append(i + 1)

    return pile