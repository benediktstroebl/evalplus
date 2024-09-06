
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
    # O(nlogn) time, O(n) space
    # sorted_array = sorted(array, key=sum)
    # return sorted_array

    # O(n) time, O(n) space
    even_sum_index = []
    odd_sum_index = []
    for index, value in enumerate(array):
        if sum(array[0:2]) % 2 == 0:
            even_sum_index.append(index)
        else:
            odd_sum_index.append(index)

    even_sum_index.sort()
    odd_sum_index.sort()

    sorted_array = []
    sorted_array = sorted_array + array[even_sum_index]
    sorted_array = sorted_array + array[odd_sum_index]

    return sorted_array

