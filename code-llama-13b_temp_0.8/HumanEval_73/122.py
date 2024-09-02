
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
    arr_size = len(arr)

    # check for empty or 1 element array
    if arr_size <= 1:
        return 0

    # check if array is already palindromic
    if is_palindromic(arr):
        return 0

    # initialize indexes for start and end of array
    start = 0
    end = arr_size - 1

    # initialize variable to store minimum changes
    changes = 0

    # run loop to check if at any position, an element can be changed to make
    # the array palindromic
    while start <= end:
        # if element at start or at end is already palindromic
        if is_palindromic([arr[start]]):
            if not is_palindromic([arr[end]]):
                # change element at end
                arr[end] = arr[start]
                changes += 1
        elif is_palindromic([arr[end]]):
            # change element at start
            arr[start] = arr[end]
            changes += 1
        else:
            # check if the element at end can be changed to the element at start
            if arr[end] == arr[start]:
                # then change the element at start
                arr[start] = arr[end]
                changes += 1
            else:
                # else, increment the counter for minimum changes by 2
                changes += 2
        start += 1
        end -= 1

    return changes

