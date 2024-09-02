
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    pal = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] / 2
        else:
            if i!= 0:
                if arr[i - 1] % 2!= 0:
                    arr[i - 1] += 1
                    arr[i] -= 1
                else:
                    arr[i] -= 1
            else:
                arr[i] -= 1
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)
        else:
            arr[i] = int(arr[i] + 1)
    for i in range(len(arr)):
        if arr[i] not in pal:
            pal.append(arr[i])
    if len(pal) == 1:
        return 0
    return len(pal) - 1

