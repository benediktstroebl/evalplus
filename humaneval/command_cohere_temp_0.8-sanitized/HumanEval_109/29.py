def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables to store the first and last values of the array
    first, last = arr[0], arr[-1]
    # Iterate over the array to compare the first and last values with the other elements
    for num in arr[1:-1]:
        if num < first or num > last:
            return False
    # If the first element is smaller than the last element, swap them
    if first > last:
        first, last = last, first
    # Check if the array can be sorted by shifting the last element to the first position
    if arr[0] == last:
        return True
    return False