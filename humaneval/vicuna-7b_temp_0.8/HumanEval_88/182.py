
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
    def sum_of_last_two(x):
        return x[-1] + x[0]

    def is_odd(x):
        return sum_of_last_two(x) % 2 == 1

    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            if is_odd(array[i]) != is_odd(array[j]):
                break
            j += 1
        if j - i == 1:
            array[i], array[j] = array[j], array[i]
            i += 1
        else:
            i += 1

    return array
