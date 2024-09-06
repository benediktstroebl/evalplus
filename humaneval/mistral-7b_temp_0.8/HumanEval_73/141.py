
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
    if len(arr) == 1:
        return 0

    size = len(arr)

    max_element = arr[size - 1]
    max_element_index = size - 1
    for i in range(size - 2, -1, -1):
        if arr[i] < max_element:
            max_element = arr[i]
            max_element_index = i

    if max_element_index % 2 == 0:
        return 0

    first_value = arr[max_element_index]
    arr[max_element_index] = max_element
    arr[size - 1] = first_value

    left, right = 0, size - 1

    while left <= right:
        if arr[left] != arr[right]:
            return 1
        left += 1
        right -= 1

    return 0

