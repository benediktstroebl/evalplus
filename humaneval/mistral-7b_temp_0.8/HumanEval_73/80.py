
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


    # Write your code here.
    count = 0
    even = 0
    odd = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > 1:
        count += 2
        arr[0] += 2
        arr[1] += 2

    if odd > 1:
        arr[0] += 1
        count += 1

    for i in range(len(arr)):
        if i == 0:
            continue
        if arr[i] == arr[i-1]:
            count += 2
            arr[i-1] += 2
            arr[i] += 2
        else:
            if arr[i] > arr[i-1]:
                arr[i] += 1
                count += 1
            else:
                arr[i-1] += 1
                count += 1

    return count

