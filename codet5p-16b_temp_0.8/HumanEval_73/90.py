
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

    # find the index of the middle element
    middle_index = len(arr) // 2

    # if the array is odd, replace the middle element with any other element
    if len(arr) % 2!= 0:
        return 1

    # if the array is even, swap the middle element with the first element
    arr[middle_index], arr[0] = arr[0], arr[middle_index]

    # this array is odd and even
    even_count = 0
    odd_count = 0

    # count the number of swaps that are needed to make it palindromic
    for index, item in enumerate(arr):
        if index < middle_index:
            if item == arr[index + 1]:
                even_count += 1
            else:
                odd_count += 1

    return min(even_count, odd_count) + 1

