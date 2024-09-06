def move_one_ball(arr):
    # If the array is empty, it's naturally sorted so return True
    if not arr:
        return True
    # Initialize variables to store the last element and the number of shifts
    last = arr[0]
    shifts = 0
    # Iterate through the array
    for curr in arr[1:]:
        # If the current element is greater than the last element, increment shifts
        if curr > last:
            shifts += 1
        # Update the last element to the current element
        last = curr
    # If the number of shifts is equal to the length of the array, it's sorted
    return shifts == len(arr)