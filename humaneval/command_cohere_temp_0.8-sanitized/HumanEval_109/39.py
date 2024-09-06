def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shifts = 0

    # Traverse the array and find the rightmost element
    for i in range(len(arr)-1, -1, -1):
        # If the element is greater than the element on its left, increase the counter by 1
        if arr[i] > arr[i-1]:
            max_shifts += 1

    # If the maximum number of right shifts is odd, it is possible to sort the array in non-decreasing order
    return max_shifts % 2 == 0