def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        integer 
    """
    # create a counter to track the number of changes
    change = 0
    # initialize the first and last indices
    first, last = 0, len(arr) - 1
    # iterate through the array and at each step compare the current element to the element at the opposite end of the array
    while first < last:
        if arr[first] != arr[last]:
            change += 1
            # increment the index of the element that needs to be changed
            first += 1
            # decrement the index of the element at the opposite end
            last -= 1
        else:
            # if the element matches at the current indices, both indices closer towards the center of the array
            first += 1
            last -= 1
    return change