
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
    l = len(arr)

    if l < 2:
        return l

    left_sum = sum(arr)
    array_sum = sum(arr)

    if left_sum % 2 == 0:
        half_sum = left_sum / 2
    else:
        half_sum = (left_sum / 2) + 1

    if array_sum % 2 == 0:
        half_array_sum = array_sum / 2
    else:
        half_array_sum = (array_sum / 2) + 1

    if array_sum > half_array_sum:
        return l

    if array_sum == half_array_sum:
        return l - 1

    if half_sum > array_sum:
        return l - 1

    middle = l / 2

    while l > 0:
        left = arr[:middle]
        right = arr[middle:]

        if sum(left) == half_sum:
            return middle
        elif sum(right) == half_sum:
            return l - middle
        elif sum(left) > half_sum:
            l -= 1
            middle -= 1
        elif sum(right) > half_sum:
            l -= middle + 1
            middle -= 1

