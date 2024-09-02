
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
    array = array[:]
    n = len(array)
    if n == 1:
        return array[0]
    odd_sums = [i+j for i,j in zip(array, [x[0] for x in reversed(array)])]
    even_sums = [i+j for i,j in zip(array, [x[0] for x in array))]
    if sum(odd_sums) % 2 == 1:
        return merge_sort(odd_sums)
    else:
        return merge_sort(even_sums)
