
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
    # your code here

    # 3 steps:
    # 1.sort ascending
    # 2.sort descending
    # 3.return sorted array

    # step 1
    # first check if the sum of first and last elements are odd or even
    # if odd: then sort ascending
    # if even: then sort descending
    # so we need to calculate the sum of first and last elements in array

    # if odd, sort ascending
    # if even, sort descending
    # so we need to calculate the sum of first and last elements in array
    # we can use python's builtin sum function to calculate the sum of first and last elements in array
    # then we need to calculate the first and last elements in array
    # we can use slicing to get the first and last elements in array
    # then we can check if the sum of first and last elements are odd or even
    # and return the sorted array

    # step 2
    # to sort descending
    # we can use the sorted function with reverse=True parameter
    # so the sorted array will
