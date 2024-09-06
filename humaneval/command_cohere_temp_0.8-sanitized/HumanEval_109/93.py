def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array in place using sorting indices
    sorting_indices = [ind for ind, num in enumerate(arr) if num == arr[0]]
    for idx in sorting_indices:
        arr[idx], arr[0] = arr[0], arr[idx]

    # Check if the array is sorted in non-decreasing order
    return all(arr[idx] <= arr[idx+1] for idx in range(len(arr)-1))