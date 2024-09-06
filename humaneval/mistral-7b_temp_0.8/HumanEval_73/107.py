
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

    # Write your code here
    arr.sort()
    count = 0
    odd_index = 0
    even_index = 0
    for i in range(len(arr)):
        if arr[i] == arr[len(arr)-1-i]:
            count += 1
        else:
            if arr[i] != arr[len(arr)-1-i]:
                if i%2 == 0:
                    even_index += 1
                else:
                    odd_index += 1
    if len(arr)%2 == 1:
        if arr[len(arr)//2] != arr[len(arr)//2+1]:
            count += 1
    if odd_index > 0:
        count += odd_index
    return count

