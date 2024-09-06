def make_a_pile(n):
    # Base case: first level has n stones
    pile = [n]
    
    # Iterate to build the pile
    while len(pile) < n + 1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    
    return pile