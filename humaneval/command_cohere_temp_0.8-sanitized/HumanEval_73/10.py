def smallest_change(arr):
    arr = list(set(arr))    # Remove duplicates to handle cases like [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    ind = len(arr) // 2     # Index of the middle element in a palindromic array
    return max(ind - arr[ind], arr[ind] - ind) + min(arr[::-1]).count(arr[::-1]) - len(arr)