def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and get the index of the last element
    arr.sort()
    last_idx = len(arr) - 1

    # Iterate through the sorted array and check for holes
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            return False

    # If the last element is not at the first index, there's a hole
    if arr[0] != arr[last_idx]:
        return False

    # If no holes found, the array can be sorted in non-decreasing order
    return True