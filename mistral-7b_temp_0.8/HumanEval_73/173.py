
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
    # Write your code here.
    new_arr = [0] * len(arr)

    for i in range(len(arr)):
        # Comparing with its element from the back
        if arr[i] != arr[-1-i]:
            new_arr[i] = 1

    # Counting the number of changes
    return sum(new_arr)

