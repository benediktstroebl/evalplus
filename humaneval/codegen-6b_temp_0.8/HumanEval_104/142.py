
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
    # taking care of edge cases
    if len(x) == 0:
        return []
    if len(x) == 1:
        if x[0] % 2 == 0:
            return []
        else:
            return [x[0]]

    x = sorted(x)
    # create a boolean array to store the value for each element
    # at each index, if the digit is even, then mark it as false
    # if it is odd, then mark it as true

    hasEven = [False] * len(x)

    # starting with the first element and skipping till the last
    # element, find the index of the first even digit
    for i in range(len(x)):
        if x[i] % 2 == 0:
            hasEven[i] = True
            break
    
    # find the index of the first odd digit
    for i in range(i, len(x)):
        if x[i] % 2 == 0 and hasEven[i - 1]:
            continue
        else:
            hasEven[i] = True
            break

    # populate the list with all elements that are even
    # and not present before the first even digit
    ans = [x[i] for i in range(len(x)) if hasEven[i] == False]
    return ans
