
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
    # Check if the array is already palindromic
    if arr[0] == arr[-1] and arr[1] == arr[-2] and arr[2] == arr[-3]:
        return 0
    # Initialize a set to keep track of the positions that need to be changed
    need_to_change = set()
    # Iterate over the array, starting from the middle
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            need_to_change.add(i)
            need_to_change.add(len(arr) - i - 1)
    # Calculate the minimum number of changes required
    return len(need_to_change)
