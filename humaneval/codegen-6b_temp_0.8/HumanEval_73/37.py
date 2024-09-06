
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
    if arr:
        min_change = 0
        if len(arr) == 1:
            return 0

        arr.sort()
        half = len(arr) / 2
        if len(arr) % 2 == 0:
            min_change = abs(arr[half] - arr[~half])
        else:
            min_change = abs(arr[~half] - arr[half])

        for i in xrange(len(arr)):
            num = arr[i]
            for i in xrange(1, len(arr)):
                while num != arr[i] and i < len(arr) - 1:
                    i += 1
                diff = abs(num - arr[i])
                if diff < min_change:
                    min_change = diff

        return min_change
    return 0

