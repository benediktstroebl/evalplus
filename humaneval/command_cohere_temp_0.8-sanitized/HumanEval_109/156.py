def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize the variable res to False
    res = False
    # Initialize the variable count to keep track of right shift operations
    count = 0
    # Iterate over the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # If the current element is smaller than or equal to the last element, increment count
        if arr[i] <= arr[len(arr) - 1]:
            count += 1
        # If the count equals the length of the array, we can get a non-decreasing array
        if count == len(arr):
            res = True
            break
    # Return the variable res
    return res