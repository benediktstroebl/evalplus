def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    m = arr[0]
    for i in range(1, n):
        if m > arr[i]:
            return False
        m = arr[i]
    return True