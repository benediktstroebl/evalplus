
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
    if not array: return []

    even_arr, odd_arr = [], []
    for index, value in enumerate(array):
        if index == 0:
            odd_arr.append(value)
        elif index == len(array) - 1:
            even_arr.append(value)
        elif not odd_arr or not even_arr:
            odd_arr.append(value) if value % 2 else even_arr.append(value)
        else:
            odd_arr.append(value) if sum(odd_arr) % 2 else even_arr.append(value)

    return even_arr if sum(odd_arr) % 2 else odd_arr

