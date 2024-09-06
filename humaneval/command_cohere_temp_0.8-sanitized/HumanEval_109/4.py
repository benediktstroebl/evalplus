def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    
    # Initialize variables for counting and checking
    moves = 0
    sorted_flag = False
    
    # Traverse through the array
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            # If unsorted, count moves and check if it can be sorted
            if not sorted_flag:
                moves += 1
                if moves == len(arr):
                    sorted_flag = True
            elif arr[i] != arr[0]:
                return False
    
    return sorted_flag