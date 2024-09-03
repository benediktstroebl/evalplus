def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones. The number of stones in the next level is:
        - the next odd number if n is odd
        - the next even number if n is even
        - starting from 1

    Return: list of stones in each level, where element at index i represents the number of stones in the level (i+1)
    """
    result = []
    for i in range(n+1):
        if n % 2 == 0:
            result.append(next_even)
        else:
            result.append(next_odd)
        next_even = 1
        next_odd = 1
        result.append(next_odd)
        next_even += 2

    return result