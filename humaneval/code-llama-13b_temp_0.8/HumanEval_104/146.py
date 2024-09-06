
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    def even_digits(number):
        """Returns True if number has any even digit. Otherwise, returns False.

        >>> even_digits(123)
        True
        >>> even_digits(2345234)
        True
        >>> even_digits(123652)
        False
        """
        while number > 0:
            if number % 2 == 0:
                return True
            number //= 10
        return False

    return sorted([num for num in x if not even_digits(num)])

