
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
    total_length = len(arr)
    if total_length <= 1:
        return 0

    mid_index = total_length // 2
    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]

    left_arr_length = len(left_arr)
    right_arr_length = len(right_arr)

    left_arr_mid = left_arr[left_arr_length // 2] if left_arr_length % 2 == 1 else left_arr[left_arr_length // 2 - 1]
    right_arr_mid = right_arr[right_arr_length // 2] if right_arr_length % 2 == 1 else right_arr[right_arr_length // 2 - 1]

    def find_diff(arr1, arr2):
        diff = 0
        for num1, num2 in zip(arr1, arr2):
            diff += abs(num1 - num2)
        return diff

    if left_arr_mid != right_arr_mid:
        return min(find_diff(left_arr, right_arr),
                   find_diff(left_arr, right_arr[::-1]) + find_diff(right_arr, left_arr))
    return find_diff(left_arr, right_arr[::-1])

