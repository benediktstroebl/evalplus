def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]
    
    # Loop to build the pile progressively
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:
            pile.append(i * 3 - 1)
        else:
            pile.append(i * 2)
    
    return pile