def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables to store the smallest and largest elements
    mini = arr[0]
    maxi = arr[0]
    for num in arr:
        # Update the smallest element if the current element is smaller
        if num < mini:
            mini = num
        # Update the largest element if the current element is larger
        if num > maxi:
            maxi = num
    # Return False if the largest element is not in the correct position (i.e., index 0)
    if maxi != arr[0]:
        return False
    # Shift the elements to the left to move the largest element to the correct position
    arr[:] = arr[-1:] + arr[:-1]
    # Check if the resulting array is in non-decreasing order
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True