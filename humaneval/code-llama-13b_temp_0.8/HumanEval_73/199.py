
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
    # Add your code here
    count = 0
    start = 0
    end = len(arr) - 1

    while start < end:
        while start < end and arr[start] == arr[end]:
            start += 1
            end -= 1
        if start < end and arr[start] != arr[end]:
            count += 2
            start += 1
            end -= 1
        else:
            break

    return count

