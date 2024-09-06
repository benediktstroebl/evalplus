
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Transform the array into the indices, as if it were 0-based
    # index = index + 1
    # Create a second array of indices to the left
    # left[i] = index of largest element <= arr[i]
    # left[-1] = -1
    # Traverse in reverse order and update left
    # left[i] = max(left[i+1], index[i])
    # right[i] = index of smallest element > arr[i]
    # right[-1] = n + 1
    # Traverse in regular order and update right
    # right[i] = min(right[i-1], index[i])
    # return -1 if left[-1] == right[0] else left[-1]
    n = len(arr)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    # Create the right array
    for i in range(n):
        right[n-1-i] = n
    for i in range(n-2, -1, -1):
        right[i] = min(right[i+1], arr[i])
    # Create the left array
    for i in range(n-2, -1, -1):
        left[i] = max(left[i+1], arr[i])
    # Check if the left and right arrays match
    for i in range(n):
        if left[i] == right[i]:
            return -1
    # Return the largest index
    return max(left)
