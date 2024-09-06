def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]

    # Iterate through odd and even levels, adjusting n accordingly
    while n != 1:
        if n % 2 == 1:
            n = n + 2
        else:
            n = n + 1

        # Append the updated number of stones for the level to the pile
        pile.append(n)

    return pile