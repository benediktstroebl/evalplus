
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
    def has_no_even_digit(x):
        """Return whether x has any even digit."""
        return not any(int(digit) % 2 == 0 for digit in str(x))

    return sorted(filter(has_no_even_digit, x))
