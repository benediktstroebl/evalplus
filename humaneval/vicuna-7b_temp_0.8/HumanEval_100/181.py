
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # pile is empty, first level is n stones
    pile = [n]
    level = 1
    while level <= n:
        # count the number of next odd numbers or even numbers
        if n % 2 == 0:
            # n is even, so n+1 is the next even number
            next_n = 2 * n + 1
            count = 0
            while next_n > 0:
                if next_n % 2 == 0:
                    count += 1
                    next_n //= 2
                else:
                    count += 1
                    next_n = next_n - 1
            # add the count of even numbers to the pile
            pile[level] = count
        else:
            # n is odd, so n+1 is the next odd number
            next_n = 2 * n + 2
            count = 1
            while next_n > 0:
                if next_n % 2 == 0:
                    count -= 1
                    next_n //= 2
                else:
                    count += 1
                    next_n -= 1
            # add the count of odd numbers to the pile
            pile[level] = count
        level += 1
    return pile
