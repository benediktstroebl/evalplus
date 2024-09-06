def make_a_pile(n):
    # Create a list to store the pile sizes
    pile = [n]
    
    # Loop to create additional pile sizes based on the given rule
    for l in range(1, n + 1):
        if l % 2 == 0 and pile[-1] % 2 == 1:
            pile.append(l + 1)
        elif l % 2 != 0 and pile[-1] % 2 == 0:
            pile.append(l + 2)
        else:
            pile.append(pile[-1] + 1)
    
    return pile