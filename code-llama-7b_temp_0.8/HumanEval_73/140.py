
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
    #print(arr)
    even = True
    for i in range(0, len(arr) - 1):
        #print(arr[i], arr[len(arr) - i - 1])
        if arr[i] != arr[len(arr) - i - 1]:
            if even:
                #print(arr[i])
                arr[i] = arr[len(arr) - i - 1]
                even = False
            else:
                arr[len(arr) - i - 1] = arr[i]
                even = True
            #print(arr)
    #print(arr)
    #print(arr[0], arr[-1])
    if arr[0] != arr[-1]:
        if even:
            arr[0] = arr[-1]
            arr[-1] = arr[0]
        else:
            arr[-1] = arr[0]
            arr[0] = arr[-1]
    if arr[0] == arr[-1]:
        even = False
    for i in range(0, len(arr) - 1):
        #print(arr[i], arr[len(arr) - i - 1])
        if arr[i] != arr[len(arr) - i - 1]:
            if even:
                #print(arr[i])
                arr[i] = arr[len(arr) - i - 1]
                even = False
            else:
                arr[len(arr) - i - 1] = arr[i]
                even = True
            #print(arr)
    #print(arr)
    #print(arr[0], arr[-1])
    if arr[0] != arr[-1]:
        if even:
            arr[0] = arr[-1]
            arr[-1] = arr[0]
        else:
            arr[-1] = arr[0]
            arr[0] = arr[-1]
    if arr[0] == arr[-1]:
        even = False
    print(arr)
    #return(arr)
    count = 0
    for i in range(0, len(arr) - 1
