
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
    # pylint: disable=invalid-name
    # pylint: disable=undefined-variable
    # pylint: disable=superfluous-parens
    # pylint: disable=no-else-return

    # Find the first non-palindrome
    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] == arr[end]:
            start += 1
            end -= 1
        else:
            break

    # Make start and end the same if the first non-palindrome is in the middle
    if start < end:
        min_changes = end - start
    else:
        min_changes = 0

    # Iterate over the array from start to end
    left_index = start
    right_index = end
    changes = 0
    while left_index < right_index:
        if arr[left_index] == arr[right_index]:
            left_index += 1
            right_index -= 1
        else:
            changes += 1

            # If there is an odd number of changes, we can move left
            if changes % 2 == 1:
                left_index += 1
            # Otherwise, move right
            else:
                right_index -= 1

    return min_changes + changes

