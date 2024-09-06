def smallest_change(arr):
    # initialize the result to the length of the array
    result = len(arr)

    # Loop through the array backwards and calculate the suffix differences from the palindrome threshold
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result = min(result, abs(i - (len(arr) - 1) - 1))

    return result
arr = [1, 2, 3, 5, 4, 7, 9, 6]