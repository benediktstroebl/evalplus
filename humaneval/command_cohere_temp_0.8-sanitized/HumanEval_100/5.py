def make_a_pile(n):
    # Base case: First level has n stones
    pile = [n]
    
    # Iterate to create subsequent levels
    while len(pile) < n + 1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    
    return pile