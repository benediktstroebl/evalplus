
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
    count = 0
    # the first element in the array
    left = arr[0]
    # the last element in the array
    right = arr[-1]

    # while there are still elements in the array
    while len(arr) > 0:
        # while the first element is less than the last
        while left < right:
            # increment the count by 1
            count += 1
            # remove the first element
            arr.pop(0)
            # remove the last element
            arr.pop(-1)
            # if there are no more elements in the array
            if len(arr) == 0:
                # return the count
                return count
            # if there are still elements in the array
            else:
                # the first element is the first element
                left = arr[0]
                # the last element is the last element
                right = arr[-1]
        # if there are more than 1 elements in the array
        if len(arr) > 1:
            # while the first element is the same as the last
            while left == right:
                # remove the first element
                arr.pop(0)
                # remove the last element
                arr.pop(-1)
                # if there are no more elements in the array
                if len(arr) == 0:
                    # return the count
                    return count
                # if there are still elements in the array
                else:
                    # the first element is the first element
                    left = arr[0]
                    # the last element is the last element
                    right = arr[-1]
