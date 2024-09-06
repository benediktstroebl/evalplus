
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
    # Check if it is palindromic
    # Check left, if match, increment both pointers
    # If no match, increment left pointer, decrement right pointer
    # Store increments as a dictionary with position as key, increments as value
    # Sum all increments and return
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 1
        else:
            return 0
    # Try to find one mismatch, if no mismatch, it is palindromic
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            break
        left += 1
        right -= 1
    if left == right:
        return 0
    # Find mismatches
    # Keep pointers
    # Increment left pointer
    # Decrement right pointer
    # Store increments as a dictionary with position as key, increments as value
    left_dict = {}
    right_dict = {}
    left_mismatches = 0
    right_mismatches = 0
    left_dict[left] = 0
    right_dict[right] = 0
    while left < right:
        if arr[left] == arr[right]:
            left_dict[left] = 0
            right_dict[right] = 0
            left += 1
            right -= 1
        elif left_mismatches > right_mismatches:
            right_dict[right] = left_dict[left]
            left_dict[left] += 1
            left += 1
            right_mismatches += 1
        else:
            left_dict[left] = right_dict[right]
            right_dict[right] += 1
            right -= 1
            left_mismatches += 1
    left_increments = sum(left_dict.values())
    right_increments = sum(right_dict.values())
    return left_increments + right_increments

