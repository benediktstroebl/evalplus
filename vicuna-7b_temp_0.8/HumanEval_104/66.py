
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
    x = list(x)
    even_digits = []
    for num in x:
        if num % 2 == 0:
            even_digits.append(num)
        else:
            even_digits.append(num // 2)
    unique_nums = [num for num in x if num not in even_digits]
    return sorted(unique_nums)
