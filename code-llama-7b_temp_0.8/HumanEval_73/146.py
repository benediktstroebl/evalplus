
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
    n = len(arr)

    def recurse(index, arr, dp):
        if index == n // 2:
            return 0
        if index in dp:
            return dp[index]
        min_palin = n
        for j in range(index, n):
            new_arr = arr[:]
            new_arr[j] = arr[index]
            new_dp = dp.copy()
            new_dp[index] = 0
            new_arr[index], new_arr[j] = new_arr[j], new_arr[index]
            new_index = index + 1
            smallest_palin = recurse(new_index, new_arr, new_dp)
            if smallest_palin + 1 < min_palin:
                min_palin = smallest_palin + 1
        dp[index] = min_palin
        return min_palin

    dp = {}
    return recurse(0, arr, dp)

