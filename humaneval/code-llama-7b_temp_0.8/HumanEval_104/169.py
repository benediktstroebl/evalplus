
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
    y = []
    for i in x:
        nums = [int(j) for j in str(i)]
        evens = [nums[k] for k in range(len(nums)) if nums[k] % 2 == 0]
        if len(evens) == 0:
            y.append(i)
    return sorted(y)
