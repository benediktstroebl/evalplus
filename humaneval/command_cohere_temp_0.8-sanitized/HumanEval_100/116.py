def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Append odd numbers to the list if n is odd, and even numbers if n is even
    if n % 2 == 0:
        pile.extend(x for x in range(n + 2, 0, -2))
    else:
        pile.extend(x for x in range(n + 1, 1, -1))
    
    return pile