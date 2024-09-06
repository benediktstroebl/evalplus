
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

    count = 0
    for i in range(len(arr)):
        temp = arr[i]
        reverse = []
        j = len(arr) - 1
        while j >= i:
            reverse.append(arr[j])
            j -= 1
        if reverse!= arr:
            count += 1
            for k in range(i+1, len(arr)):
                if arr[k] == temp:
                    arr[k] = arr[i]
                    break
    return count
