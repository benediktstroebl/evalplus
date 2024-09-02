
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
    if len(array) == 0:
        return array

    length = len(array)
    mid = length // 2

    if sum(array[:2]) % 2 == 0:
        return sort_array(array[::-1])

    if length <= 2:
        return array

    # sum(array[:mid]) > sum(array[mid:])
    if sum(array[:mid]) > sum(array[mid:]):
        return sort_array(array[mid:]) + sort_array(array[:mid])
    # sum(array[:mid]) < sum(array[mid:])
    return sort_array(array[mid:]) + sort_array(array[:mid])

    # def sort_array(array):
    #     if len(array) <= 2:
    #         return array

    #     result = []
    #     even = sum(array[:2]) % 2 == 0
    #     if even:
    #         for i in range(0, len(array), 2):
    #             result.append(array[i])
    #         for i in range(1, len(array), 2):
    #             result.append(array[i])
    #     else:
    #         for i in range(len(array) - 1, -1, -2):
    #             result.append(array[i])
    #         for i in range(len(array) - 2, -1, -2):
    #             result.append(array[i])

    #     return sort_array(result)
