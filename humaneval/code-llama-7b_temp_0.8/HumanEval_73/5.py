
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
    # print("arr",arr)
    l = []
    arr_len = len(arr)
    #print("len",arr_len)
    for i in range(0, int(arr_len/2)):
        #print("i", i)
        if arr[i] != arr[arr_len-1-i]:
            l.append(1)
        #print("arr[i]", arr[i])
        #print("arr[arr_len-1-i]", arr[arr_len-1-i])
    #print(l)
    if len(l) > 0:
        return sum(l)
    return 0

