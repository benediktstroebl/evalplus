def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]
    
    # Loop to create additional levels
    for i in range(1, n // 2 + 1):
        # If the current level is even, increment the previous even level
        if i % 2 == 0:
            pile.append(pile[-1] + 2)
        # If the current level is odd, increment the previous odd level
        else:
            pile.append(pile[-1] + 1)
    
    return pile