
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

    def is_palindromic(arr):
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

    result = 0
    if is_palindromic(arr):
        return result
    # Fill array
    all_nums = set()
    for num in arr:
        all_nums.add(num)

    for num in arr:
        for candidate in all_nums:
            arr_copy = list(arr)
            arr_copy[arr.index(num)] = candidate
            if is_palindromic(arr_copy):
                return result + 1
        result += 1
    return result

