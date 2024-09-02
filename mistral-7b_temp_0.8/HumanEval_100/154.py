
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
    #TODO: Write your solution here

    oddlist = [1, 3, 5, 7, 9, 11, 13, 15]
    evenlist = [2, 4, 6, 8, 10, 12, 14, 16]
    if n % 2 == 0:
        return evenlist[n//2]
    else:
        return oddlist[n//2]




