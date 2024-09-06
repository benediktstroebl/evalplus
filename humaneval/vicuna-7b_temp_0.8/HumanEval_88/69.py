
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    def sum_is_odd(arr):
        sum = 0
        for i in arr:
            sum += i
        return sum % 2 == 1

    def swap_odd_and_even(arr):
        even = 0
        odd = len(arr) - 1
        while even <= odd:
            if arr[even] % 2 == 0:
                arr[even], arr[odd] = arr[odd], arr[even]
                odd -= 1
                even += 1
        return arr

    def reverse_array(arr):
        return arr[::-1]

    def sort_array_helper(arr):
        if sum_is_odd(arr):
            return swap_odd_and_even(arr)
        else:
            return arr

    return sort_array_helper(array)