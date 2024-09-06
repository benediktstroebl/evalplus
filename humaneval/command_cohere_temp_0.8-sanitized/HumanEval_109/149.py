def move_one_ball(arr):
    # If the array is empty, it's naturally sorted so return True
    if not arr:
        return True
    # Sort the array
    arr.sort()
    # Verify if the sorted array is non-decreasing
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))