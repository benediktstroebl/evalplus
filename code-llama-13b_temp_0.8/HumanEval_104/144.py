
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

    even_digits = set()

    for number in x:
        number_str = str(number)
        for digit in number_str:
            if int(digit) % 2 == 0:
                even_digits.add(number)
                break

    return sorted([n for n in x if n not in even_digits])
