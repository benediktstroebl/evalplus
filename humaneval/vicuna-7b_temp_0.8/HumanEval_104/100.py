
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
    # sort the input list
    x.sort()
    # reverse the input list
    x = x[::-1]
    # find the sum of all elements in the reversed list
    sum = 0
    for x in x:
        sum += x
    # check if the sum is odd
    if sum % 2 == 1:
        # reverse the list again
        x = x[::-1]
        # find the index of the first non-zero element
        start = 0
        while sum[start] == 0:
            start += 1
        # initialize a variable to store the index of the first non-zero element
        first_non_zero = start
        # iterate through the list and mark each element that is not even
        for i in range(1, len(x)):
            if sum[i] % 2 == 0:
                x[i] = x[i] % 2
                # remove the mark from the element in front of the current element
                if first_non_zero == i-1:
                    x[first_non_zero] = 0
                # update the first non-zero element
                first_non_zero = i
    return x
