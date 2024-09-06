def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if len(arr) == 0:
        return True

    # Initialize variables for the first and last elements
    first, last = arr[0], arr[-1]

    # Iterate through the array to find the largest gap
    for n in range(1, len(arr)):
        if arr[n] > arr[n - 1]:
            gap = abs(arr[n] - arr[n - 1])
        elif arr[n] < arr[n - 1]:
            gap = abs(arr[n - 1] - arr[n])
        else:
            gap = 0

        # If the gap is larger than the difference between the first and last elements,
        # it's possible to sort the array by moving one ball
        if gap > abs(last - first):
            first, last = arr[n], arr[n]

    # If the largest gap is still 0 (all identical elements), it's sorted
    if gap == 0:
        return True

    # If the above loop didn't update first and last, it's not possible to sort
    return False