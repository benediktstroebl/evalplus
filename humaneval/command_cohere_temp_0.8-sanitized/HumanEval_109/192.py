def move_one_ball(arr):
    n = len(arr)
    # We try to move through the array with increments of (n - 1) to
    # check if any element travels through all positions. If this is the
    # case for any element, it is impossible to sort the array
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j] == arr[j + 1]:
                cnt += 1
                if cnt == n - 1:
                    return False
            else:
                cnt = 0
        if arr[0] == arr[n - 1]:
            return False
    return True