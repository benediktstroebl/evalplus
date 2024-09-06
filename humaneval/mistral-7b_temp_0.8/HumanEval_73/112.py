
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

    # Create an array to store the frequency of each element in the input array
    freq = [0] * len(arr)

    # Count the frequency of each element
    for i in range(len(arr)):
        freq[arr[i] - 1] += 1

    # Count the number of elements that need to be changed to make the array palindromic
    min_changes = 0
    for i in range(len(arr) // 2):
        # If the frequency of the elements on the left side is not equal to the frequency
        # of the elements on the right side, we need to make changes to make the array palindromic
        if freq[i] != freq[len(arr) - i - 1]:
            min_changes += abs(freq[i] - freq[len(arr) - i - 1])

    return min_changes
