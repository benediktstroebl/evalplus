def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Loop through and calculate the number of stones for each subsequent level
    while len(pile) < (n + 1):
        if pile[-1] % 2 == 1:  # if current level has an odd number of stones
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    
    return pile