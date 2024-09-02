
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
    #######################################
    # PROBLEM EXPLANATION
    # -----------------------------------------------------------------
    # here's an overview of the solution:
    # * we'll create two copies of the given array.
    # * we'll sort one array in ascending order.
    # * we'll sort the other array in descending order.
    # * we'll then return one array or the other based on the
    #   criteria described in the problem.
    # * we'll sort the arrays by calling the merge_sort
    #   method recursively.
    # * we'll do that by calling the merge_sort method
    #   recursively on both arrays and passing down the
    #   sub-arrays.
    # * we'll merge the sub-arrays by calling the merge
    #   method recursively.
    # * we'll do that by calling the merge method recursively
    #   on both sub-arrays and passing down the sub-sub-arrays.
    #######################################
    # BRUTE FORCE SOLUTION
    # -----------------------------------------------------------------
    # * use a for loop to iterate through the array.
    # * use an if statement to check if the sum of the
    #   first element and last element is odd or even.
    # * if the sum is odd, return the array in ascending order.
    # * if the sum is even, return the array in descending order.
    # * else, return the array as is.
    #######################################
    # RECURSIVE SOLUTION
    # -----------------------------------------------------------------
    # * use the merge_sort method recursively on both arrays.
    # * pass down the sub-arrays to the merge_sort method recursively.
    # * use the merge method recursively.
    # * pass down the sub-sub-arrays to the merge method recursively.
    #######################################
    if not array:
        return array

    asc_arr = array.copy()
    asc_arr = merge_sort(asc_arr)
    desc_arr = array.copy()
    desc_arr = merge_sort(desc_arr, False)

    
