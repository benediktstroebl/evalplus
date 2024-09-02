
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

    sorted_array = []
    odd_even_index = 0 if sum(array) % 2 == 0 else 1
    odd_even_value = array[-1] if sum(array) % 2 == 0 else array[0]

    if odd_even_index:
        for i in range(len(array)):
            if array[i] <= odd_even_value:
                sorted_array.append(array[i])

        for i in range(len(array)):
            if array[i] > odd_even_value:
                sorted_array.append(array[i])

    else:
        for i in range(len(array)):
            if array[i] >= odd_even_value:
                sorted_array.append(array[i])

        for i in range(len(array)):
            if array[i] < odd_even_value:
                sorted_array.append(array[i])

    return sorted_array
