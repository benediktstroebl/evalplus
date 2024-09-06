def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables for the first and last elements
    first, last = arr[0], arr[-1]
    # Iterate over the array to compare elements
    for num in arr[1:-1]:
        if num < first:
            first = num
        elif num > last:
            last = num
    # Check if the array can be sorted by shifting elements to the right
    if first <= last:
        return True
    else:
        return False