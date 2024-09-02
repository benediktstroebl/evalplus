
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
    if not array:
        return array

    res = array.copy()
    odd, even = 0, 1
    # sweep first and last index
    # when first and last index have same parity, then reverse the res array
    while odd < len(res) and even < len(res):
        if sum(res[odd], res[-even]) % 2:
            res[odd], res[even] = res[even], res[odd]
        if odd == even:
            res.reverse()
            return res
        odd += 1
        even += 1
