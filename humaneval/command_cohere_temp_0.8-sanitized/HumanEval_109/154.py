def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    arr_sort = sorted(arr)
    return arr == arr_sort