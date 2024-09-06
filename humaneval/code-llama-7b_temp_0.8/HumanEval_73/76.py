
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
    if len(arr) <= 1:
        return 0

    midpoint = len(arr) // 2
    # Copy the first half of the array into a stack
    first_half = []
    for i in range(0, midpoint):
        first_half.append(arr[i])

    # Copy the second half of the array into a list
    second_half = []
    for i in range(midpoint, len(arr)):
        second_half.append(arr[i])

    # Reverse the second half
    second_half.reverse()

    # For each item in the first half, check to see if its corresponding item
    # in the second half is the same, and if not, count it as one change
    count = 0
    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            count += 1

    return count

