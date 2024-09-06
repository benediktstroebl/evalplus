
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
    n = len(array)
    # base case: if the array is empty, return an empty array
    if n == 0:
        return []
    # find the middle index
    middle = (n // 2) - 1
    # sum of odd numbers from 0 to n-1
    odd_sum = sum([x for x in range(0, n) if x % 2 == 1])
    # sum of even numbers from 0 to n-1
    even_sum = sum([x for x in range(0, n) if x % 2 == 0])
    # check if odd_sum is odd
    if odd_sum % 2 != 0:
        # if odd_sum is odd, all numbers are sorted in descending order
        return sorted(array, reverse=True)
    # if odd_sum is even, sort the array in ascending order
    return sorted(array)