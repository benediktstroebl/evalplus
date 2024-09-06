def move_one_ball(arr):
    arr.sort()
    return arr == list(range(len(arr)))