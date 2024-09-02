
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
    # worst case is the array is already palindromic
    if is_palindrome(arr):
        return 0

    # set the value of the "end" index
    end_index = len(arr) - 1

    # get the halfway index
    half_index = len(arr) // 2

    # initialize a variable to store the number of changes
    num_changes = 0

    # while the left index isn't the same as the right index
    while end_index > half_index:
        # if the left index is not equal to the right index
        if arr[end_index] != arr[half_index]:
            # increment the number of changes
            num_changes += 1
        # otherwise
        else:
            # move the end index inward
            end_index -= 1
            # and move the halfway index outward
            half_index += 1

    # return the number of changes
    return num_changes

