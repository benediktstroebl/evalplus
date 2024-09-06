def move_one_ball(arr):
    if len(arr) == 0:
        return True
    
    n = len(arr)
    # calculate the number of shifts needed to arrange inIncreasing order
    required_shifts = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            required_shifts += 1
    
    return required_shifts == 0