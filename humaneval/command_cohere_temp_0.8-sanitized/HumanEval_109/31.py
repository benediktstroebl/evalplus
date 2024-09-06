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
    # Return False if the largest element is not in the correct position (index 0)
    if maxi != arr[0]:
        return False
    # Return True if the smallest element is in its correct position (last position)
    return mini == arr[-1]