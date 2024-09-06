def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array in place using sorting values from bisect module
    # This ensures the array is sorted in non-decreasing order
    arr.sort(key=lambda x: bisect.bisect_left(arr, x))

    # If the sorted array has elements in order, return True
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))