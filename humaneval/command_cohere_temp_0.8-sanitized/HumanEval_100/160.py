def make_a_pile(n):
    # Create a list to store the number of stones in each level
    pile = [0] * (n + 1)
    
    # Define the number of stones in the first level (the number of 'n')
    pile[0] = n
    
    # Iterate through the pile to create the rest of the levels
    for l in range(1, n + 1):
        # If the level is odd, take the next odd number
        if l % 2 == 1:
            pile[l] = l + 2
        
        # If the level is even, take the next even number
        else:
            pile[l] = l + 1
    
    return pile