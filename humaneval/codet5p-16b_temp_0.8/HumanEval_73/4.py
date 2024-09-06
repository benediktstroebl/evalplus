
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

    arr_size = len(arr)
    max_num = max(arr)
    min_num = min(arr)
    count_array = [0] * (max_num - min_num + 1)
    result = arr_size
    for num in arr:
        count_array[num - min_num] += 1

    for i in range(len(count_array)):
        count = count_array[i]
        if 2 * count < result:
            result = 2 * count

    return result

