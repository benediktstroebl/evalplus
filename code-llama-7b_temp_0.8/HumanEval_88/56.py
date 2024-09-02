
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
    # init
    res = list()
    # iterate the array
    for index in range(len(array)):
        # while res is not empty
        while len(res) > 0:
            # check if sum( first index value, last index value) is odd
            if sum(res[0], array[index]) % 2:
                # insert the value at the end of the list
                res.insert(len(res), array[index])
                break
            else:
                # insert the value at the front of the list
                res.insert(0, array[index])
                break
        else:
            # when res is empty, directly append the value to the array
            res.append(array[index])
    return res

