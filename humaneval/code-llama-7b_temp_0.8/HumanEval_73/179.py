
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
    r = [0] * 10001  # To store the count of the elements
    for i in arr:
        r[i] += 1
    odd_num = 0  # To count the number of odd numbers
    count = 0
    for i in range(len(r)):
        count += (r[i] // 2)
        if r[i] % 2 != 0:
            odd_num += 1
    if odd_num % 2 == 0:
        return count
    else:
        return count + 1

