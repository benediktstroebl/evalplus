def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Compute the number of stones for the next level depending on the parity of n
    while len(pile) < (len(str(n)) - 1) // 2:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    
    return pile