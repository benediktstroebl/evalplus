def move_one_ball(arr):
    if len(arr) == 0:
        return True
    count = 0
    for i in range(len(arr)):
        if i > 0 and arr[i] > arr[i - 1]:
            count += 1
    return count % len(arr) == 0