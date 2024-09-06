
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
    if len(arr) <= 1:
        return 0
    # if all elems are equal, this is a palindrome
    # for example, [1, 1, 1, 1, 1]
    if arr == arr[::-1]:
        return 0

    # find the first elem that's not equal to the last
    # for example, [1, 1, 1, 2, 1, 1, 1]
    middle_index = 0
    while arr[middle_index] == arr[-1 - middle_index]:
        middle_index += 1

    # get the elements from both ends to the middle
    first_half = arr[:middle_index + 1]
    second_half = arr[middle_index + 1:][::-1]
    # for example, [1, 1, 1, 2, 1, 1, 1]
    # first_half = [1, 1, 1]
    # second_half = [1, 1, 1]
    #
    # now compare the first half and second half
    # to find the number of elems we need to change
    # to make this array palindrome
    # for example, [1, 1, 2, 1, 1, 1]
    # first_half = [1, 1]
    # second_half = [1, 1]
    # -> 2
    result = 0
    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            result += 1
    return result

