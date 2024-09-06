
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
    def get_max_value(arr):
        max_value = 0
        for i in arr:
            if i > max_value:
                max_value = i
        return max_value

    max_val = get_max_value(arr)
    min_val = get_max_value(arr)

    res = []
    for i in arr:
        if i == max_val:
            res.append(min_val)
        else:
            res.append(i + 1)
    return min(res)

