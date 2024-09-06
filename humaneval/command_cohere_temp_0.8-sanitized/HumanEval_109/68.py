def move_one_ball(arr):
    n = len(arr)
    arr.sort()
    return n == len(set(arr)) and arr[0] <= arr[1]