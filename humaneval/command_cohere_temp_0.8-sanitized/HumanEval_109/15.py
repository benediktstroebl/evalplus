def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Initialize the variable should_swap to False
    should_swap = False

    # Iterate over the array
    for i in range(len(arr)):
        # If the current element is greater than the last element, set should_swap to True
        if i == 0 and arr[i] > arr[len(arr) - 1]:
            should_swap = True
        # If the current element is less than the last element, return False
        elif arr[i] < arr[len(arr) - 1]:
            return False

    # If should_swap is True, return True
    return should_swap