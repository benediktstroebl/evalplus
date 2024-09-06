def move_one_ball(arr):
    # if the array is empty, it is always possible to sort it
    if not arr:
        return True

    # sort the array and remove duplicates
    arr.sort()
    arr = list(set(arr))
    
    # find the largest index i such that arr[i] == arr[i+1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] == arr[i+1]:
            return False

    return True