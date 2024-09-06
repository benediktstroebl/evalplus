
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
    stack = [0] * n
    d = [0] * (n+1)
    piles = [0] * (n+1)
    for i in range(1, n+1):
        d[i] = (i+1) % 2
        piles[i] = len(stack)
        for j in range(piles[i]):
            if d[i] == 0:
                stack.append(0)
                continue
            n = d[i-1] + d[i]
            if n % 2 == 0:
                for k in range(piles[i-1]):
                    stack[piles[i-1]-k] = 0
            else:
                for k in range(piles[i-1], piles[i]):
                    stack[piles[i-1]-k] = 0
    return stack
