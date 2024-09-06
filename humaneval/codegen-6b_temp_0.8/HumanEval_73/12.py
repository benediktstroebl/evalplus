
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
    # if the array is already a palindrome, just return 0
    if is_palindrome(arr):
        return 0

    # if the length of the array is 1, return 0
    if len(arr) == 1:
        return 0

    # map each element to the index it is on
    elements = {element: arr.index(element) for element in arr}

    # map the absolute value of each element to the index it is not on
    abs_elements = {element: abs(arr.index(element)) for element in arr}
    abs_elements = {element: abs_elements[element] for element in arr}

    # we can make the array palindrome by either changing an element to the index of its
    # absolute value or by changing the absolute value of an element to its index
    changes = 0
    for element in arr:
        if abs_elements[element] < elements[element]:
            abs_elements[element] += 1
            changes += 1
        else:
            elements[element] += 1

    return changes

