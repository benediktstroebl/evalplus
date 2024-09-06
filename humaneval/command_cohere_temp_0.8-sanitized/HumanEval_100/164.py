def make_a_pile(n):
    # Create a list to store the pile size at each level
    pile = [n]
    
    # Loop through odd levels
    for i in range(1, (n // 2) + 1):
        pile.append(2 * i - 1)

    # Loop through even levels
    for i in range(1, (n // 2) + 1):
        pile.append(2 * i)

    return pile