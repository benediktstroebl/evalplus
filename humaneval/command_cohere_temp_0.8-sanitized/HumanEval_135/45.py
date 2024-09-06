def can_arrange(arr):
    prev = arr[0]
    maxi = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1] and arr[i] != arr[i - 1]:
            maxi = i + 1
    if maxi == len(arr) or arr[maxi] == arr[maxi - 1]:
        return -1
    else:
        return maxi