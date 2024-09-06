
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
    # initialize variables
    even_list = []
    odd_list = []
    even_list_size = 0
    odd_list_size = 0

    # Split list into even and odd list
    for i in range(len(arr)):
        if i % 2 == 0:
            even_list.append(arr[i])
            even_list_size += 1
        else:
            odd_list.append(arr[i])
            odd_list_size += 1

    if even_list_size == odd_list_size:
        return 0
    elif even_list_size == odd_list_size + 1:
        return odd_list_size
    else:
        return odd_list_size + 1
