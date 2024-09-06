def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Loop to create each level of the pile
    for i in range(1, n+1):
        # If the current level is odd, the next level will contain the next odd number of stones
        if i % 2 == 1:
            pile.append(i + 1)
        # If the current level is even, the next level will contain the next even number of stones
        else:
            pile.append(i + 2)
    
    return pile