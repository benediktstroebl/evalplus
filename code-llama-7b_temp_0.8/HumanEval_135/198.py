
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    arr_len = len(arr)
    if arr_len == 0:
        return 0
    if arr_len == 1:
        return -1

    # Check if the array is descending or not
    arr_diff = [x - y for x, y in zip(arr, arr[1:])]
    if all(x > 0 for x in arr_diff):
        return -1

    # Find the first element that is greater than it's previous element
    start_idx = -1
    for i in range(1, arr_len):
        if arr[i] >= arr[i-1]:
            start_idx = i-1
            break

    # If no element greater than it's previous element is found return -1
    if start_idx == -1:
        return -1

    # Initialize end_idx, start searching from index of first greater element
    end_idx = start_idx
    for i in range(start_idx+1, arr_len):
        if arr[i] < arr[i-1]:
            end_idx = i-1
            break

    # If end_idx is -1 then all elements are greater than previous one
    if end_idx == -1:
        end_idx = arr_len - 1

    # arr[start_idx] is the first element greater than previous
    # arr[end_idx] is the last element greater than previous
    # Find the largest index between these two elements
    max_idx = start_idx
    for i in range(start_idx+1, end_idx+1):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

