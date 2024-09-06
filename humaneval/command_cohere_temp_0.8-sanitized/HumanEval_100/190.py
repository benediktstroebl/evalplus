def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]

    # If n is odd, add the next two odd numbers to the pile
    if n % 2 == 1:
        pile.extend([n + 2, n + 4])
    # If n is even, add the next two even numbers to the pile
    else:
        pile.extend([n + 1, n + 3])

    return pile