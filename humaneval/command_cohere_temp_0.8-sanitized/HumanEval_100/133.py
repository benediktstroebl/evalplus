def make_a_pile(n):
    # Determine the number of stones in the first level
    stones_first_level = n
    
    # Create a list to store the number of stones in each level
    pile = [stones_first_level]
    
    # Iterate through levels 2 through n+1
    for l in range(2, n + 2):
        # If the current level is odd, use the next odd number
        if l % 2 == 1:
            pile.append(l + 1)
        # If the current level is even, use the next even number
        else:
            pile.append(l + 2)
    
    return pile