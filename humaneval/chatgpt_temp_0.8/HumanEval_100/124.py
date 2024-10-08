def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).
    """
    
    pile = [n]
    stones = n
    for i in range(n-1):
        if stones % 2 == 0:
            stones += 1
        else:
            stones += 2
        pile.append(stones)
    return pile
