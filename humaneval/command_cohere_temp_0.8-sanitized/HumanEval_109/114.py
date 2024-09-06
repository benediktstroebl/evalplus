def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Initialize variables for the first and last elements
    first, last = arr[0], arr[-1]

    # Iterate through the array to find the rightmost element and compare it to the elements before it.
    for n in range(1, len(arr)):
        if arr[n] < arr[n - 1]:
            first = min(first, arr[n])

    # Iterate through the array to find the leftmost element and compare it to the elements after it.
    for n in range(len(arr) - 2, -1, -1):
        if arr[n] > arr[n + 1]:
            last = max(last, arr[n])

    # If the first element is less than or equal to the last element, it's possible to sort the array in non-decreasing order.
    return first <= last