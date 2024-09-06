def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Iterate through odd and even levels according to the given criteria
    if n % 2 == 0:  # n is even
        pile.extend(n + 2j for j in range(1, (n // 2) + 1))
    else:
        pile.extend(n + 2j - 1 for j in range(1, (n // 2) + 1))
    
    return pile