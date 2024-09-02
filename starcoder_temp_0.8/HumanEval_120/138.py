
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    assert len(arr) >= 1

    # If k is greater than the length of arr, then return the sorted list of all the elements in arr.
    if k > len(arr):
        return sorted(arr)

    # Otherwise, partition the array into two halves.
    left_half = arr[: len(arr) // 2]
    right_half = arr[len(arr) // 2 :]

    # Recursively find the k largest elements in the left half of arr.
    left_k_largest = maximum(left_half, k)

    # Recursively find the k largest elements in the right half of arr.
    right_k_largest = maximum(right_half, k)

    # The final result is the k largest elements in either the left or right halves, but not both.
    return _merge(left_k_largest, right_k_largest, k)

