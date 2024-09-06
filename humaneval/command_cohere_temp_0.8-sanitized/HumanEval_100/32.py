def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Calculate the number of stones for the next level if n is odd
    if n % 2 == 1:
        pile.append(n + 2)
    else:
        pile.append(n + 1)
    
    return pile