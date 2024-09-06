def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Compute the number of stones for the next level depending on the parity of n
    while n != 1:
        if n % 2 == 1:
            n = n + 2
        else:
            n = n + 1
    
        # Append the computed number of stones to the pile
        pile.append(n)
    
    return pile