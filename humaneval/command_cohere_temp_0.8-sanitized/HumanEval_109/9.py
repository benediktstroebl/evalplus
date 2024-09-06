def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Initialize indices to track the smallest and second smallest elements
    i_smallest = 0
    i_second_smallest = 1

    # Initialize count of right shifts needed
    shift_count = 0

    # Iterate through the array to find the smallest and second smallest elements
    for i in range(1, len(arr)):  # Start the loop from index 1 as the first element is already at index 0
        if arr[i] < arr[i_smallest]:
            i_second_smallest = i_smallest
            i_smallest = i
        elif arr[i] < arr[i_second_smallest]:
            i_second_smallest = i

    # If second smallest element is not the last element in the array, it's possible to sort in non-decreasing order
    if i_second_smallest != len(arr) - 1:
        return True

    # If it's not possible to perform a single right shift to obtain non-decreasing order, return False
    if arr[i_smallest] < arr[i_second_smallest]:
        return False

    # Otherwise, we need to perform a right shift to obtain non-decreasing order
    shift_count = len(arr) - 2 - i_second_smallest
    return shift_count >= 0