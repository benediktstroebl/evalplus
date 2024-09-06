def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    
    # Initialize the variable should_swap to False, it will be set to True
    # if any two elements in the array are in the wrong order.
    should_swap = False
    
    # Iterate over the array to check if any two elements are in the wrong order.
    for i in range(1, len(arr)):
        # If the current element is less than the next element, they are in the wrong order.
        if arr[i] < arr[i-1]:
            should_swap = True
            break
    
    # If should_swap is still False at the end of the loop, the array is already in non-decreasing order.
    # Since we assume the list has unique elements, any swap will result in a wrong order.
    return not should_swap