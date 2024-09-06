
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
    # convert the list to a set for faster membership check
    set_arr = set(arr)

    # count the number of unique elements in the list
    n = len(set_arr)

    # initialize variables to keep track of the minimum number of changes
    min_changes = n
    min_change = n

    # iterate through the list, trying to make one change at a time
    for i in range(1, n):
        # find the index of the next smallest element
        j = (i + n) % n
        while j != i:
            j += 1
        next_smallest_index = j

        # check if the current element is the next smallest element
        if arr[i] == arr[next_smallest_index]:
            # if it is, update the element and move on to the next one
            arr[i] = arr[j]
            next_smallest_index = j
            continue

        # if the current element is not the next smallest element, update the next smallest element
        arr[next_smallest_index] = arr[j]
        next_smallest_index = j

        # update the number of changes
        min_changes -= 1
        min_change = min(min_change, next_smallest_index - i + 1)

    return min_changes, min_change
