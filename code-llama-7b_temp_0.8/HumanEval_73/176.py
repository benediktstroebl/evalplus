
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
    # calculate the number of mirrored characters
    mirrored_characters = sum([1 for char in arr if char == arr[-1 * (char - 1)]])
    # calculate the number of non-mirrored characters
    non_mirrored_characters = len(arr) - mirrored_characters
    # return the number of elements that need to be changed
    return non_mirrored_characters if non_mirrored_characters <= mirrored_characters else mirrored_characters





