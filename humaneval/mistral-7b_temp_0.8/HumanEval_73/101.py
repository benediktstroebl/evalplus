
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

    # if length of the list is odd, then there is no palindromic list
    if len(arr) % 2 == 1:
        return -1

    # Keep track of the number of elements that need to be changed
    count = 0

    # Keep track of the current maximum element
    max_element = arr[0]

    # Keep track of the current minimum element
    min_element = arr[0]

    # Loop through the list
    for num in arr:
        # If the current element is larger than the maximum element, update the maximum element
        if num > max_element:
            max_element = num

        # If the current element is smaller than the minimum element, update the minimum element
        if num < min_element:
            min_element = num

        # If the current element is larger than the minimum element, and smaller than the maximum element, then
        # it needs to be changed to the minimum element to make the list palindromic
        if num > min_element and num < max_element:
            count += 1

    #
