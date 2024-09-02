
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

    # O(n) time, O(n) space
    # reverse the array
    # count # of occurrences in the original
    # count # of occurrences in reverse
    # find the minimum number to make it palindrome
    # return the number of elements that need to be changed

    if not arr:
        return 0
    # reverse the array
    reverse = arr[::-1]

    # count # of occurrences in the original
    occurrences = {}
    for item in arr:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1

    # count # of occurrences in reverse
    reverse_occurrences = {}
    for item in reverse:
        if item in reverse_occurrences:
            reverse_occurrences[item] += 1
        else:
            reverse_occurrences[item] = 1

    # find the minimum number to make it palindrome
    minimum = len(arr)
    for key in occurrences:
        if key in reverse_occurrences:
            needed = occurrences[key] + reverse_occurrences[key] - 2 * min(occurrences[key], reverse_occurrences[key])
            minimum = min(needed, minimum)
        else:
            needed = occurrences[key]
            minimum = min(needed, minimum)
    return minimum
