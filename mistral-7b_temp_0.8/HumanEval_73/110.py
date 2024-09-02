
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
    # add your code here
    # a = arr.copy()
    # a.sort()
    # a1 = a.copy()
    # a1.reverse()
    # ans = 0
    # # print(a)
    # # print(a1)
    # for i in range(len(a)):
    #     if a[i] != a1[i]:
    #         ans += 1
    # return ans
    a = arr.copy()
    a.sort()
    a1 = a.copy()
    a1.reverse()
    ans = 0
    # print(a)
    # print(a1)
    for i in range(len(a)):
        if a[i] != a1[i]:
            ans += 1
    return ans
