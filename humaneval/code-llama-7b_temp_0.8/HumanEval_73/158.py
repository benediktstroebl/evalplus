
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
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i])
        new_arr.append(arr[len(arr) - i - 1])
    print(new_arr)
    count = 0
    for i in range(len(new_arr) - 1):
        if new_arr[i] != new_arr[i+1]:
            count += 1
    return count

