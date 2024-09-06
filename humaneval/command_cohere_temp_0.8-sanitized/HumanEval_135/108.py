def can_arrange(arr):
    largest = -1
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            largest = i+1
    return largest