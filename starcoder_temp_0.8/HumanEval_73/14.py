
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
    # O(N)
    # calculate all palindrome substrings.
    palindrome_substrings = [arr[i: j] for i in range(n) for j in range(i + 1, n + 1) if is_palindrome(arr[i: j])]

    # O(N^2)
    # count the number of changes required for each substring.
    change_count = [0] * len(palindrome_substrings)
    for i in range(len(palindrome_substrings)):
        for j in range(len(palindrome_substrings[i])):
            if palindrome_substrings[i][j]!= arr[j]:
                change_count[i] += 1

    return min(change_count)
