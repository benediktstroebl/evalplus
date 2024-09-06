def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Consider all possible palindromic arrays and minimize the changes required
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            result = min(result, count_changes(arr))
            arr[i], arr[j] = arr[j], arr[i]
    
    return result
def count_changes(arr):
    # Count changes required to make array palindromic
    # Remove duplicates and add 1 for each duplicate element
    return len(set(arr)) + len(set(reversed(arr))) - 2 * len(set(arr))