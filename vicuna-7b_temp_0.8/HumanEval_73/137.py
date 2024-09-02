
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
    n = len(arr)
    min_change = float('inf')
    min_index = 0

    for i in range(1, n):
        for j in range(i):
            # swap two elements
            for k in range(j + 1, n):
                arr[k], arr[j] = arr[j], arr[k]

        # check if the array is palindrome
        if arr[i] == arr[n - i - 1]:
            # swap the element at index i with any element in the range [i+1, n]
            for k in range(i + 1, n):
                arr[k], arr[i] = arr[i], arr[k]

        # update the minimum change and index
        change = abs(arr[0] - arr[n - 1])
        if change < min_change:
            min_change = change
            min_index = i

    return min_change