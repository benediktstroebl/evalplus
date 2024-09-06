def can_arrange(arr):
    ans = -1
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            return i
        if arr[i] > arr[i+1]:
            ans = i
    return ans