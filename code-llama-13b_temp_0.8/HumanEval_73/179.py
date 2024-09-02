
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
    if len(arr) <= 2:
        return 0

    first_half = arr[: len(arr) // 2]
    second_half = arr[len(arr) // 2 :]

    # The first index where the element is different
    first_difference_index = len(first_half) - 1
    for index in range(len(first_half)):
        if first_half[index] != second_half[-1 - index]:
            first_difference_index = index
            break

    # Find the reversed first first_difference_index elements
    # that are equal to first_half
    reversed_first_half = first_half[first_difference_index :]
    reversed_first_half.reverse()

    # We need to change the first_difference_index number of elements
    # because we have to change all the elements after first_difference_index
    # in the second_half to make it equal to reversed_first_half
    return first_difference_index
