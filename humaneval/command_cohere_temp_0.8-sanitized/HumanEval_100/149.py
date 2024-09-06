def make_a_pile(n):
    # Create a list to store the number of stones in each level
    pile = [0] * (n + 1)
    
    # The first level has n stones
    pile[0] = n
    
    # Calculate the number of stones in the next level
    for i in range(1, n + 1):
        if i % 2 == 1:  # If the current level is odd (starting from the second level)
            pile[i] = i + 2  # Add 4 to the current level
        else:
            pile[i] = i + 1  # Else add 1 to the current level
    
    return pile