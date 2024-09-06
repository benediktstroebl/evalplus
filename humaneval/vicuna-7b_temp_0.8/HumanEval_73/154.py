
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
    for i in range(n):
        for j in range(i, n):
            # Check if the substring from index i to j is a palindrome
            if j + 1 == n or arr[i] != arr[j]:
                # If not, increase the change
                change = abs(n - i - 1) + abs(n - j)
                if change < min_change:
                    min_change = change
    return min_change
