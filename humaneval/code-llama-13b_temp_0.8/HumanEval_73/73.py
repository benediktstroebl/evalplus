
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
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 1
        return 0

    odd_count = 0
    odd_position = []
    even_count = 0
    even_position = []

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd_count += 1
            odd_position.append(i)
        else:
            even_count += 1
            even_position.append(i)
    if odd_count == 0:
        return 0
    if even_count == 0:
        return odd_count
    if odd_count == 1:
        return min(odd_count, even_count)
    if odd_count == 2:
        if len(odd_position) == 2:
            if abs(odd_position[1] - odd_position[0]) == 1:
                return odd_count
        return min(odd_count, even_count)

    # we have more than 2 odd numbers
    if len(odd_position) == 2:
        if abs(odd_position[1] - odd_position[0]) == 1:
            return odd_count - 1

    # we have more than 2 odd numbers
    if len(odd_position) > 2:
        count_change_odd = odd_count - 1
        count_change_even = even_count
        if len(odd_position) > 3:
            count_change_odd = odd_count - 2
        return min(count_change_odd, count_change_even)

    return odd_count

