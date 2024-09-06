def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]
    
    # Loop to construct the pile incrementally
    for i in range(1, n // 2 + 1):
        pile.append(pile[i - 1] if i % 2 else i)
    
    return pile