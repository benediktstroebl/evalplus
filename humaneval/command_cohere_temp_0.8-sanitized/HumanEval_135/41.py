def can_arrange(arr):
    ind = len(arr) - 2
    while ind >= 0 and arr[ind] >= arr[ind + 1]:
        ind -= 1
    return -1 if ind == -1 else ind + 1