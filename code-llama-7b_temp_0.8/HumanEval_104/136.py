
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
    # Your code here
    even = set()
    for num in x:
        num_str = str(num)
        for char in num_str:
            if int(char) % 2 == 0:
                even.add(num)
                break
    return sorted(list(set(x) - even))

