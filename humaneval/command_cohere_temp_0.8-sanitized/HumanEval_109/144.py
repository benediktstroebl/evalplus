def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shifts = 0

    # Traverse the array and find the rightmost element
    for i in range(len(arr)-1, -1, -1):
        # Count shifts required for this element to get to index 0
        max_shifts = max(max_shifts, arr[i] - i)

    # Check if any element requires more than 1 shift, which would make the sorting impossible
    return max_shifts <= 1