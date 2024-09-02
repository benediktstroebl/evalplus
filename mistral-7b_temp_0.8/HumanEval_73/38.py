
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
    # Make a copy of the array to avoid mutating the original
    arr_copy = arr.copy()

    # Find the minimum number of changes needed to make the array palindromic
    min_changes = 0
    while not is_palindrome(arr_copy):
        min_changes += 1
        # Find the smallest element in the array
        min_index = find_smallest(arr_copy)
        # Find the largest element in the array
        max_index = find_largest(arr_copy)
        # Swap the smallest and largest elements
        arr_copy[min_index], arr_copy[max_index] = arr_copy[max_index], arr_copy[min_index]

    return min_changes
