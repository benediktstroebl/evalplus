
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
    num = len(arr)
    half = num // 2 + num % 2
    arr = arr[:half]

    # if all odd, make even
    if num % 2 != 0:
        arr.append(0)

    arr.reverse()

    diff = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    if len(set(diff)) == 1:
        return len(arr) - num // 2 - 1
    else:
        return min(len(arr) - i for i in range(1, len(arr)) if diff[i] == 0)
