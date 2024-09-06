
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
    def find_smallest_change(arr):
        if len(arr) == 1:
            return 0

        max_val = max(arr)

        for i in range(len(arr)):
            if arr[i]!= arr[i + 1]:
                arr[i + 1] = max_val
                find_smallest_change(arr[:i] + arr[i + 2:])

    find_smallest_change(arr)
    return arr.count(max(arr))

