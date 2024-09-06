def make_a_pile(n):
    # Base case: if n is 0, return a list with a single element, n.
    if n == 0:
        return [0]

    # Initialize an array to hold the stones in each level.
    pile = [n]

    # Iterate through levels 1 to n, ensuring that the number of stones at each level follows the problem specification.
    for level in range(1, n):
        # If the current level is odd, the next level will have the next odd number of stones.
        if level % 2 == 1:
            pile.append(pile[level] + 1)
        # If the current level is even, the next level will have the next even number of stones.
        else:
            pile.append(pile[level] + 2)

    return pile