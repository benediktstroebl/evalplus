def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]
    
    # Loop to create additional pile levels
    for i in range(1, n.bit_length() + 1):
        # If the current level is odd, take the next odd number
        if i % 2 == 1:
            pile.append(next_odd(pile[i - 1]))
        # If the current level is even, take the next even number
        else:
            pile.append(next_even(pile[i - 1]))
    
    return pile
def next_odd(n):
    return n + 2
def next_even(n):
    return n + 1