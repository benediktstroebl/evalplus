
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
    if len(arr) == 0:
        return 0

    odd_count = 0
    even_count = 0
    odd_ind = 0

    for index in range(len(arr)):
        if arr[index] != arr[len(arr)-1-index]:
            odd_count += 1
            odd_ind = index
        if arr[index] != arr[index+1]:
            even_count += 1

    if odd_count % 2 == 0:
        return min(odd_count, even_count)
    else:
        return min(odd_count, even_count + 2)
