
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
    if len(arr) < 2:
        return 0
    arr = list(arr)

    def check_palindromic(arr):
        """
        Check if the given array is palindromic
        """
        return arr == arr[::-1]

    # Now we need to calculate the min number of elements to remove to make the array palindromic
    start, end = 0, len(arr) - 1

    while start < end:
        # when we have an even length array
        # we cannot remove elements from the beginning
        if len(arr) % 2 == 0:
            check_index = len(arr) // 2
        else:
            check_index = len(arr) // 2 + 1

        # when we have an odd length array
        # we must have 1 element that needs to be removed from the front
        if len(arr) % 2 == 1:
            check_index -= 1

        if check_palindromic(arr[start:check_index]) and check_palindromic(arr[check_index:end]):
            # we can remove the first element
            start += 1
        else:
            # we have to remove the middle element
            end -= 1

    return len(arr) - start
