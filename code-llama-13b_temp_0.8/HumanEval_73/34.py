
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
    if len(arr) == 1:
        return 0

    if len(arr) == 2:
        return 0 if arr[0] == arr[1] else 1

    # Find first non matching pair
    i = 0
    j = len(arr) - 1
    while arr[i] == arr[j] and i < j:
        i += 1
        j -= 1

    if i == j:
        return 0

    # We need to find the number of letters in the left substring
    # that occur in the right substring, and the right substring.
    # For this, we just scan the two substrings and check.
    # For each number in the left substring, we keep a counter of the number of occurrences in the right substring
    left_occurrences = {k: 0 for k in range(10)}
    for i in range(i, len(arr)):
        left_occurrences[arr[i]] += 1

    right_occurrences = {k: 0 for k in range(10)}
    for j in range(0, j + 1):
        right_occurrences[arr[j]] += 1

    # At this point we have two dictionaries. The number of letters in the
    # left substring that occur in the right substring is the min of the
    # difference between left_occurrences[k] and right_occurrences[k] for all k
    to_change = 0
    for k in left_occurrences.keys():
        to_change += min(left_occurrences[k], right_occurrences[k])

    # Now we need to find the number of remaining letters in the right substring
    # that occur in the left substring. These letters need to be removed from the right substring.
    to_change += sum([right_occurrences[k] for k in left_occurrences.keys() if left_occurrences[k] > right_occurrences[k]])

    return to_change

