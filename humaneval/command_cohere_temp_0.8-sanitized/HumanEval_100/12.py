def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]
    
    # Compute the number of stones for the next level if n is even
    while n % 2 == 0:
        n = n // 2
        pile.append(n)
    
    # Compute the number of stones for the next level if n is odd
    while n % 2 != 0:
        n = (n + 1) // 2
        pile.append(n)
    
    return pile