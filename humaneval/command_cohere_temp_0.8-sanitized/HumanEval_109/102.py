def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Traverse through the array and check if any element is greater than the last element
    for i in range(len(arr) - 1):
        if arr[i] > arr[-1]:
            return False

    # If no larger element is found, it's possible to achieve sorted order
    return True