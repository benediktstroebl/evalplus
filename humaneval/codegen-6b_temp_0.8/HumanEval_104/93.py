
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
    numbers = []
    for number in x:
        if str(number).isdigit():
            if str(number)[-1] == '2' or str(number)[-1] == '4' or str(number)[-1] == '6':
                continue
            else:
                numbers.append(number)

    numbers.sort()
    return numbers

