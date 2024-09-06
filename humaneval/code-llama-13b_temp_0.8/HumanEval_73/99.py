
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
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0

    count_changes = 0
    max_int = max(arr)
    int_count = [0] * (max_int + 1)

    # find how many times each number appears
    for i in range(len(arr)):
        int_count[arr[i]] += 1

    # we want to find the number that appear one time and delete
    # all other numbers that appear
    number_appear_once = 0

    for i in range(1, len(int_count)):
        if int_count[i] % 2 == 1:
            if number_appear_once == 0:
                number_appear_once = i
            else:
                count_changes += int_count[i]
                int_count[i] = 0

    if number_appear_once != 0:
        count_changes += int_count[number_appear_once] - 1
        int_count[number_appear_once] = 0

    for i in range(len(int_count)):
        count_changes += int_count[i] // 2

    return count_changes

