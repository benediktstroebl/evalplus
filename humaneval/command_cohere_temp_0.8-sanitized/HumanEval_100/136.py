def make_a_pile(n):
    # Initialize a list to store the pile sizes
    pile = [n]

    # Loop to create additional pile levels
    for i in range(1, n // 2 + 1):
        pile.append(2 * i - 1 if i % 2 else 2 * i)

    return pile