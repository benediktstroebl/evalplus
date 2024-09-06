def smallest_change(arr):
    # Initialize the result to zero or the worst case
    result = len(arr) // 2
    for i in range(len(arr)):
        # Try to find a palindrome by toggling the i'th element
        temp = arr.copy()
        temp[i] = arr[::-1][i]
        if temp == sorted(temp):
            result = min(result, 1)
        else:
            # If it's not a palindrome, toggle it back
            temp[i] = arr[i]
            arr[i] = arr[::-1][i]
    return result