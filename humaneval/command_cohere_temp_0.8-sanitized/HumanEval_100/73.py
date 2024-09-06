def make_a_pile(n):
    # Create a list to store the pile size at each level
    pile = [n]
    
    # Loop to create the pile with the specified number of levels
    for i in range(1, n + 1):
        # If the current level is odd, increment the previous odd level
        if i % 2 == 1:
            pile.append(pile[-1] + 2)
        # If the current level is even, increment the previous even level
        else:
            pile.append(pile[-1] + 1)
    
    return pile