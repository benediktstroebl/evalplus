def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    
    # Initialize the count of elements that have correct order when shifted to index 0.
    # Example: For [3, 4, 5, 1, 2], the count is 2 (3 and 4).
    correct_order_count = 0
    
    for i in range(n):
        # If the current element is less than or equal to the element at index 0, increment the count.
        if arr[i] <= arr[0]:
            correct_order_count += 1
    
    return correct_order_count == n