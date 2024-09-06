def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Consider all elements one by one
    for i in range(len(arr)):
        # Try making all elements equal to the i'th element
        for e in arr:
            test_arr = arr.copy()
            test_arr[i] = e
            test_arr[i ^ 1] = e
            if test_arr == sorted(test_arr):
                result = min(result, 1)
                break
    
    return result