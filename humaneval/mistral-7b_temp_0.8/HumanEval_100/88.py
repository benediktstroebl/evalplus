
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

    # your code here
    # we will first create an empty list
    my_list = []
    for i in range(0,n):
        if n%2 == 0:
            # if n is even
            my_list.append(2*i+2)
        else:
            # if n is odd
            my_list.append(2*i+3)
    return my_list

