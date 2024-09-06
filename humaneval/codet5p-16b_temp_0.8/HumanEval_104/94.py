
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

    def check_even(number):
        """Return True if number has any even digit"""
        number = str(number)
        for i in number:
            if int(i) % 2 == 0:
                return True
        return False

    def digit_list(number):
        """Return a list of digits from number"""
        number = str(number)
        return [int(i) for i in number]

    return sorted(set(filter(lambda x: not check_even(x), digit_list(x))))



