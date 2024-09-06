def can_arrange(arr):
    ans = -1
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            ans = i+1
            break
    return ans