def move_one_ball(arr):
    # If the array is empty, it's naturally sorted so return True
    if not arr:
        return True
    # Make a copy of the list to maintain the original order
    arr = arr[:]
    # Sort the array
    arr.sort()
    # Return False if the sorted array is not in non-decreasing order
    if arr[0] >= arr[1]:
        return False
    # Shift all elements in the array by one position to achieve non-decreasing order
    arr[1:] = arr[1:][1:]
    # Return True if the shifted array is in non-decreasing order
    return arr[0] <= arr[1]