def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]
    
    # Loop to create additional levels according to the problem specification
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:  # If the level index is odd
            pile.append(i * 3 - 1)  # Add the next odd number
        else:
            pile.append(i * 2)  # Add the next even number
    
    return pile