
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
    def get_sum_and_sort(array):
        n = len(array)
        if n < 1:
            return array
        elif n == 1:
            return [array[0]]
        elif n == 2:
            return [array[1], array[0]] if sum(array) % 2 == 1 else [array[0], array[1]]
        else:
            left_sum = sum(array[:n // 2])
            right_sum = sum(array[n // 2:])
            if left_sum % 2 == 1:
                left_array = get_sum_and_sort(array[:n // 2])
                right_array = get_sum_and_sort(array[n // 2:])
                right_array.reverse()
                return left_array + right_array
            else:
                left_array = get_sum_and_sort(array[:n // 2])
                left_array.reverse()
                right_array = get_sum_and_sort(array[n // 2:])
                return left_array + right_array

    return get_sum_and_sort(array)
