def make_a_pile(n):
    # Create a list to store the number of stones in each level
    pile = [n]
    
    # If n is odd, add the next odd number to the pile
    if n % 2 == 1:
        pile.append(n + 2)
    # If n is even, add the next even number to the pile
    else:
        pile.append(n + 1)
    
    # Return the pile
    return pile