
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
    # If the array is palindromic, return 0
    if is_palindrome(arr):
        return 0

    # When the array is not palindromic, if the array has only two elements,
    # return the number of elements to be changed
    if len(arr) == 2:
        return abs(arr[0] - arr[1])

    # The minimum number of elements to change
    min_num_elements_to_change = None

    # Get the middle index
    middle_index = len(arr) // 2

    # Get the first half
    first_half = arr[:middle_index]

    # Get the second half
    second_half = arr[middle_index:]
    second_half.reverse()

    # Calculate the minimum number of elements to change in the first and second half
    first_half_min_num_elements_to_change = smallest_change(first_half)
    second_half_min_num_elements_to_change = smallest_change(second_half)

    # Get the minimum number of elements to change
    min_num_elements_to_change = min(first_half_min_num_elements_to_change, second_half_min_num_elements_to_change)

    return min_num_elements_to_change + 2

