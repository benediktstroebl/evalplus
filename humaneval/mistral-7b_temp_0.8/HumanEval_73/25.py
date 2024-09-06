
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
    # TODO: Write your code here
    count=0
    l=len(arr)
    l1=l
    count_even=0
    count_odd=0
    for i in arr:
        if i%2==0:
            count_even=count_even+1
        else:
            count_odd=count_odd+1
    if count_even==0 or count_odd==0:
        return count
    for i in range(l1):
        if arr[i]!=arr[l-i-1]:
            count=count+1
    return count
