def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Consider all possible element swaps
    for i in range(len(arr)):
        # Swap the current element with all other elements in the array
        for j in range(len(arr)):
            # Swap the elements and recompute the result
            arr[i], arr[j] = arr[j], arr[i]
            result = min(result, count_changes(arr))
            arr[i], arr[j] = arr[j], arr[i]
    
    return result
def count_changes(arr):
    # Initialize the result to zero
    result = 0
    
    # Count changes required for each element to make it match its mirror element
    for i in range(len(arr)):
        result += (arr[i] != arr[len(arr) - 1 - i])
    
    return result