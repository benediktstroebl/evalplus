def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array.
    shift_count = 0

    # Iterate through the array and count the number of elements in the wrong order.
    for i in range(1, len(arr)): 
        if arr[i] < arr[i - 1]:
            shift_count += 1
        elif arr[i] > arr[i - 1]:
            return False

    # If no elements are out of order, or if the number of shifts is less than the length of the array, it's possible to sort.
    return shift_count <= len(arr)