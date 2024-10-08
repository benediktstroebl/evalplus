
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
    for _ in range(10):
        print(arr)
        if is_palindromic(arr):
            return 0
        indices = []
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                indices.append(i)
        if not indices:
            return len(arr) - 1
        arr[min(indices)] += 1
        for index in reversed(sorted(indices)):
            arr[index] -= 2
    return 0
