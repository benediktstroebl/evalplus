
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
    # Mirror the array
    # Count the differences between the two halves
    # The answer is the sum of the differences
    # If the two halves are the same, the answer is 0
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left.reverse()
    right.reverse()
    diffs = []
    for i in range(len(left)):
        if left[i] != right[i]:
            diffs.append(right[i] - left[i])
    return sum(diffs)

