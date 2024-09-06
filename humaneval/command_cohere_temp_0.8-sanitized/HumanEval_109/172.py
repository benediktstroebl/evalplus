def move_one_ball(arr):
    n = len(arr)
    arr.sort()
    expected = [0] * n
    expected[0] = arr[-1]
    expected[-1] = arr[0]
    for i in range(1, n):
        expected[i] = expected[i - 1]
    return expected == arr