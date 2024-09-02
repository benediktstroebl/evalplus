
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
    list1 = [x // 10 ** i for i in range(1, len(str(x)))]
    list2 = [int(str(x)) % 10]
    result = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if (list1[i] * 10 + list2[j]) % 10 != int(str(x)) % 10:
                result.append(list1[i])
                result.append(list2[j])
                break
    return result
