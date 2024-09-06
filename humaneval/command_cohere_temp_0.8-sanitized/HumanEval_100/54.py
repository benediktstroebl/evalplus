def make_a_pile(n):
    # Create a list to store the pile sizes
    pile = [n]
    
    # Loop to create additional pile sizes based on the given rule
    while len(pile) < (1 + n): 
        if len(pile) % 2 == 0: 
            pile.append(pile[-1] + 2)
        else: 
            pile.append(pile[-1] + 1)
    
    return pile