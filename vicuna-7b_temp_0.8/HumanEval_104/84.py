
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
    n = len(x)
    even_index = [i for i in range(n)]
    even_index.remove(i)
    for i in range(1, n):
        if i not in even_index:
            result.append(x[i])
            even_index.append(i)
    return result
