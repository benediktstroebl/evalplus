def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Initialize variables for the first and last elements
    first, last = arr[0], arr[-1]

    # Iterate through the array to find the rightmost element and compare with the first
    for num in arr[1:-1]:
        if num > first:
            first = num

    # If the first element is greater than the rightmost element, it's possible to sort
    if first <= last:
        return True

    # If it's not possible to sort, perform a right shift operation
    arr = arr[1:] + [last]

    # Recursively check if the new array can be sorted
    return move_one_ball(arr)