def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)

    # Consider the first and last element as they require one change to be palindromic
    if arr[0] != arr[-1] : 
        result = min(result, 1 + smallest_change(arr[1:-1])) 
        
    # Consider all adjacent pairs of elements that are not equal
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]: 
            result = min(result, 1 + smallest_change(arr[:i] + [arr[i]+1] + arr[i+1:]))

    return result