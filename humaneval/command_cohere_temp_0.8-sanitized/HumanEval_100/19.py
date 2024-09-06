def make_a_pile(n):
    # Create a list to store the number of stones in each level
    pile = [n]
    
    # Loop through the levels of the pile
    for i in range(1, n+1):
        # Add the next odd number to the pile if the current level is odd
        if i % 2 == 1:
            pile.append(i + 2)
        # Add the next even number to the pile if the current level is even
        else:
            pile.append(i + 1)
    
    return pile