
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
    # res = []
    # if array == []:
    #     return res
    # res.extend(array)
    # even_odd_sum = sum(res[0], res[-1])
    # if even_odd_sum % 2 == 0:
    #     res = sorted(res, reverse=True)
    # else:
    #     res = sorted(res, reverse=False)
    # return res

    # Another Solution
    # return sorted(array, key=lambda i: (sum(i) % 2, i))
    # Return the same array for [] or []
    if len(array) == 0:
        return array
    res = []
    for i in range(len(array)):
        if sum(array[i]) % 2 == 0:
            res.append(array[i])
        else:
            res.insert(0, array[i])
    return res
