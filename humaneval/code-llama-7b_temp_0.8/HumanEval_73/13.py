
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
    n = len(arr)
    even = n % 2 == 0
    center = n // 2
    right = n - center - 1 if even else n // 2

    left, right, center = arr[:center], arr[center:], []
    if even:
        left = [num for num in left if num != right.pop()]

    return len(left) + len(right)

