
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
    assert n > 0
    # your code here
    numbers = []
    even_numbers = []
    odd_numbers = []
    for number in range(1, n+1):
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    odd_numbers.reverse()
    even_numbers.reverse()
    numbers = even_numbers + odd_numbers
    return numbers
