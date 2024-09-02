
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
    if not arr or len(arr) == 0:
        return 0

    # O(n)
    # We will use the left half of the array as a hash map. For each left element, we will store
    # the number of elements to the right of it that have the same value.
    # For example, for arr = [1, 2, 3, 3, 2] we have:
    # left_hash = {
    #   1: 4
    #   2: 3
    #   3: 1
    # }
    left_hash = {}
    for i in range(len(arr) // 2):
        # If we haven't seen this value before, we set it to 1 (right_len = 1)
        left_hash[arr[i]] = left_hash.get(arr[i], 1)
        # If we have seen this value before, we increment it by 1
        left_hash[arr[i]] += 1

    # O(n)
    # Here, we will use the right half of the array as a hash map. For each right element, we will
    # store the number of elements to the left of it that have the same value.
    # For example, for arr = [1, 2, 3, 3, 2] we have:
    # right_hash = {
    #   1: 1
    #   2: 3
    #   3: 4
    # }
    # Since the right half is the mirror image of the left half, we can start from the second to last
    # element and work backwards.
    right_hash = {}
    # right_idx is the first index of the right half of the array.
    right_idx = len(arr) // 2
    for i in range(len(arr) // 2, len(arr)):
        # If we haven't seen this value before, we set it to 1 (left_len = 1)
        right_hash[arr[i]] = right_hash.get(arr[i], 1)
        # If we have seen this value before, we increment it by 1
        right_
