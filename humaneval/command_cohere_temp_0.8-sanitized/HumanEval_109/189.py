def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    
    # Initialize the count of right shifts required
    count = 0
    
    # Initialize an array to store the seen elements in the circular buffer.
    # Each element in this array will be False initially.
    seen = [False] * (n)
    
    # For each element in the array
    for i in range(n):
        # If the element is not seen before, set the seen array to True at the
        #  index where the element will be after right shifts.
        if not seen[i % n]:
            seen[i % n] = True
            count += 1
    
    # Return False if the count of right shifts is larger than n-1
    return count <= n - 1