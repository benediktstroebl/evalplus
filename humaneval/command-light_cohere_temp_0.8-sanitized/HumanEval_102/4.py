def choose_num(x, y):
    if x > y:
        return x
    if x < y or y < 0:
        return -1
    mid = (x + y) // 2
    if mid % 2 == 0:
        return mid
    return y