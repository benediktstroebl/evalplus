
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
    total = 0
    num_changes = 0
    # Iterate over every element in the array
    for i in range(len(arr)):
        # Skip even numbers because we don't have to change them
        if arr[i] % 2 == 0:
            continue
        # If element is odd, compare it to the reverse of the array at the same index
        else:
            num_changes += abs(arr[i] - arr[len(arr) - i - 1])

    return num_changes

