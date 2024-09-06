
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
    if not x: return None
    x_str = [str(n) for n in x]
    x_str_uniq = list(set(x_str))
    even_num = lambda n: '0' in n or '2' in n or '4' in n or '6' in n or '8' in n
    x_uniq_even = filter(even_num, x_str_uniq)
    return sorted(map(int, filter(lambda n: not even_num(n), x_str_uniq)))

