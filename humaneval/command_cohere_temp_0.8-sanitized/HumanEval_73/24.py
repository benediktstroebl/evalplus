def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Consider all the elements one by one and minimize the result accordingly
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # Consider all pairs of elements (arr[i], arr[j])
            for val1 in arr:
                for val2 in arr:
                    # Swap arr[i] and arr[j] to get the palindrome
                    arr[i], arr[j] = val2, val1
                    if arr == arr[::-1]:
                        result = min(result, 1)
                        break
                else:
                    # If no palindrome is found, break out of the loop
                    # to avoid unnecessary computations
                    break
    
    return result