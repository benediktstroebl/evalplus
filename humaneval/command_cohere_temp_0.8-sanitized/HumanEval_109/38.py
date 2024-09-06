import random
def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    arr_copy = arr.copy()
    random.shuffle(arr_copy)
    for i in range(n-1):
        if arr_copy[i] > arr_copy[i+1]:
            return True
        elif arr_copy[i] < arr_copy[i+1]:
            return False
    return True