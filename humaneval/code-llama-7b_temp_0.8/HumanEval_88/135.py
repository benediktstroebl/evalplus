
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
    # 先找出數組的長度以及數組的前後兩個index值
    len_of_array = len(array)
    front_value = array[0]
    back_value = array[len_of_array - 1]
    # 假設數組長度是偶數, 依照偶數的規則排序
    if len_of_array % 2 == 0:
        front_value = array[0]
        back_value = array[len_of_array - 1]
        result = sorted(array, key = lambda x: (x - front_value) * (x - back_value))
    # 假設數組長度是奇數, 依照奇數的規則排序
    elif len_of_array % 2 == 1:
        result = sorted(array, key = lambda x: (x - front_value) * (x - back_value), reverse = True)
    return result
