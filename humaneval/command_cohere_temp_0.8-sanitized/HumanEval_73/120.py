def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Consider all the elements one by one and minimize the result accordingly
    for i in range(len(arr)):
        # Try all elements from index 0 to i and minimize the result
        result = min(result, abs(arr[i] - palindrome_close(arr, i)[0]))
    
    return result
def palindrome_close(arr, i):
    # Initialize the candidate and its index
    candidate, j = arr[i], i
    
    # Try all elements from index 0 to i in the array as the candidate
    for k in range(len(arr)):
        if k != j and arr[k] == candidate:
            candidate, j = arr[k], k
    
    # Return the candidate and its index if it is the closest palindrome, otherwise return the default value
    return [candidate, j] if arr[j] != candidate else [arr[0], 0]