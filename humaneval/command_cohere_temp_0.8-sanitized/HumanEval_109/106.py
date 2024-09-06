def move_one_ball(arr):
    res = False
    cnt = 0
    for i in range(1, len(arr)):   
        if arr[i] < arr[i - 1]: 
            cnt += 1
            # Shift elements to the right by one to make arr[i] move to index 0
            arr = arr[-1:] + arr[:-1]    # Using tuple unpacking and inplace list modification
            if cnt == 1: res = True    # If a single shift was enough, it is possible to sort the array in non-decreasing order
    return res