def move_one_ball(arr):
    arr.sort()
    if arr[0] >= arr[1]:
        return True
    else: 
        return False