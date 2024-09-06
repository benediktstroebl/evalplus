
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
    palindrome = False
    length = len(arr)
    new_arr = []
    for i in range(length):
        if i > length - 1 - i:
            palindrome = True
    if palindrome == True:
        return 0

    for i in range(length - 1):
        if arr[i] != arr[length - 1 - i]:
            new_arr.append(arr[i])
            new_arr.append(arr[length - 1 - i])
            # print(new_arr)
            return len(new_arr)
    return len(new_arr)

