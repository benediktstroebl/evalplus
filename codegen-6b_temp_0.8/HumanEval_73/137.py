
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
    for i in range(len(arr)//2):
        print(arr[i],arr[-1-i])
        if arr[i] != arr[-1-i]:
            count += 1
    return count

assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1,2,3,4,3,2,2]) == 1
assert smallest_change([8,9,10,3,7,7,2,7,7,6,3]) == 7
assert smallest_change([1,2,3,4,3,2,2]) == 0
assert smallest_change([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 10
assert smallest_change([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]) == 0
assert smallest_change([1,2,3,4,3,2,2]) == 0
assert smallest_change([1,2,3,4,3,2,2,1]) == 1
assert smallest_change([11,8,5,4,3,2,1]) == 3
assert smallest_change([1,2,3,4,3,2,2,1,1,1]) == 1
assert smallest_change([12,4,7,0,11,6,8,5,7,1,8]) == 3
assert smallest_change([11,6,8,5,7,1,8,4,7,0,11,6,8,5,7,1,8]) == 1
assert smallest_change([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,