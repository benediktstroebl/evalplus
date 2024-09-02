
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

    # Create an array to hold the number of times each element in the input array appears
    arr_counts = [0] * 10000

    # Iterate through the input array and update the counts for each element
    for num in arr:
        arr_counts[num] += 1

    # Iterate through the counts array and check for pairs of elements that can be used to make the array palindromic
    count = 0
    for i in range(10000):
        if arr_counts[i] > 0 and arr_counts[9999 - i] > 0:
            count += min(arr_counts[i], arr_counts[9999 - i])
            arr_counts[i] -= min(arr_counts[i], arr_counts[9999 - i])
            arr_counts[9999 - i] -= min(arr_counts[i], arr_counts[9999 - i])

    # Return the number
