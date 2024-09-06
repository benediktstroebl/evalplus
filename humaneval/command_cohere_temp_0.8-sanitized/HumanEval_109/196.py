def move_one_ball(arr):
    num = len(arr) - 1
    while arr[num] > arr[num - 1]:
        if num == 0:
            return False
        num -= 1
    
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True