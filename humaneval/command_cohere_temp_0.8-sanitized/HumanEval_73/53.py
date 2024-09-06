def smallest_change(arr):
    # Initialize the smallest change to an excessively large value
    smallest_change = float('inf')
    
    # Calculate the smallest change for reversing the array
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            count_reversal = 0
            for k in range(len(arr)):
                if arr[k] != arr[len(arr) - 1 - k]:
                    count_reversal += 2  # Value to be changed and its mirror-image value in reverse array
            smallest_change = min(smallest_change, count_reversal)
            arr[i], arr[j] = arr[j], arr[i]  # Swap back to original arrangement

    return smallest_change