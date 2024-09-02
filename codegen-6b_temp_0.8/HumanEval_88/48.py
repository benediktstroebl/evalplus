
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
    a = array
    if len(a) <= 1:
        return a
    left, right = a[ : len(a) / 2], a[len(a) / 2 : ]
    left_sum, right_sum = sum(left), sum(right)
    if left_sum == right_sum:
        return left + right
    elif left_sum != right_sum:
        return left + sorted(right, reverse=True)

