
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
    # Initialise variables
    length = len(arr)
    left_index = 0
    right_index = length - 1
    largest_diff = 0
    # Loop through array
    while left_index < right_index:
        # if the first value is lower than the last, we need to check the difference and find the largest
        if arr[left_index] < arr[right_index]:
            diff = arr[right_index] - arr[left_index]
            if diff > largest_diff:
                largest_diff = diff
            # Move left_index and right_index up one
            left_index += 1
            right_index -= 1
        # if the last value is lower than the first, we need to check the difference and find the largest
        elif arr[left_index] > arr[right_index]:
            diff = arr[left_index] - arr[right_index]
            if diff > largest_diff:
                largest_diff = diff
            # Move left_index and right_index down one
            left_index -= 1
            right_index += 1
        # else they are equal and we do not need to do anything
        else:
            # Move left_index and right_index up one
            left_index += 1
            right_index -= 1
    return largest_diff

