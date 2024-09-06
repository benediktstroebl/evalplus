
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
    digit_list = [int(i) for i in str(x)]
    even_digits = [i for i in digit_list if i % 2 == 0]
    return sorted(digit_list[i:], key=lambda x: x // 2) for i in range(len(even_digits))