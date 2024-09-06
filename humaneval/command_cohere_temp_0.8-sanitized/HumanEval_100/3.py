def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]
    
    # Loop to create additional levels
    for i in range(1, n):
        # If the current level is odd, the next level will contain the next odd number of stones
        if i % 2 == 1:
            pile.append(i + 3)
        # If the current level is even, the next level will contain the next even number of stones
        else:
            pile.append(i + 2)
    
    return pile