def can_arrange(arr):
    prev = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[index] and arr[i] < arr[index + 1]:
            index = i
        elif arr[i] >= arr[index] and arr[i] > arr[index + 1]:
            return index
        elif arr[i] < arr[index] and arr[i] >= arr[index + 1]:
            index += 1
        prev = arr[index]
    return -1 if index == len(arr) - 1 and arr[index] >= arr[index + 1] else index