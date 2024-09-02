
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
    arr_length = len(arr)
    if arr_length == 1:
        return 0
    elif arr_length == 2:
        return abs(arr[0] - arr[1])
    else:
        i = 0
        j = arr_length - 1
        # this list is going to keep track of the costs of the smallest change to the palindromic array.
        costs = [abs(arr[i] - arr[j])]

        # start the search at index i+1, because the first element is handled separately.
        while i < j - 1:
            # swap if the absolute difference between the elements is less than the smallest cost yet so far.
            costs.append(min(abs(arr[i] - arr[j]), abs(arr[j] - arr[i])))
            if abs(arr[i] - arr[j]) < abs(arr[j] - arr[i]):
                i += 1
            else:
                j -= 1

        # add out the absolute difference between the last two elements of the array.
        costs.append(abs(arr[i] - arr[j]))
        return min(costs)
