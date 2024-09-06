
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Hash map to store the number of occurrences of each number
    occurrences = {}
    # count the occurrences of each number
    for n in arr:
        if n not in occurrences:
            occurrences[n] = 1
        else:
            occurrences[n] += 1
    # minimum number of changes is either the number of odd occurrences, or
    # the number of even occurrences minus the number of occurrences of the
    # middle number
    if occurrences[max(occurrences, key=occurrences.get)] % 2 == 0:
        return max(occurrences.values()) - 2
    return max(occurrences.values()) - 1
