
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
    #  Check if a number has an even digit
    def has_even_digits(n):
        for num in str(n):
            if int(num) % 2 == 0:
                return True
        return False

    #  Get all numbers with no even digits
    no_even_digits = []
    for n in x:
        if has_even_digits(n) == False:
            no_even_digits.append(n)

    #  Sort the list
    no_even_digits.sort()

    return no_even_digits

