
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

    mid_index = len(arr) // 2
    left = arr[:mid_index]
    right = arr[mid_index + 1 :][::-1]
    if right == left:
        return 0
    left_elements = {el: 0 for el in left}
    right_elements = {el: 0 for el in right}
    for i, el in enumerate(left):
        if el in right_elements:
            left_elements[el] = i + 1
            right_elements[el] = i + 1
    for i, el in enumerate(right):
        if el in left_elements:
            left_elements[el] = i + 1
            right_elements[el] = i + 1
    if len(left_elements) != len(right_elements):
        return -1
    return sum(left_elements.values())

