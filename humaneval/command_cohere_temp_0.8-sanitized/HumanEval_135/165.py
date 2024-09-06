def can_arrange(arr):
    ind = len(arr) - 2
    while ind >= 0 and arr[ind] >= arr[ind + 1]:
        ind -= 1
    return max(ind + 1, -1)