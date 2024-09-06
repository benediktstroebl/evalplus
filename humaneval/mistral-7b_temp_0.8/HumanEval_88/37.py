
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

    # INSERT CODE HERE.
    # return list_sorted

    # list_sorted = array.sort()
    # print(list_sorted)

    # if (array[0] + array[-1]) % 2 == 0:
    #     list_sorted = array.sort(reverse=True)
    # else:
    #     list_sorted = array.sort()
    # return list_sorted

    # list_sorted = array.sort(reverse= (array[0] + array[-1]) % 2 == 0)
    # return list_sorted

    # list_sorted = array.sort(reverse= (array[0] + array[-1]) % 2 == 0)
    # return list_sorted

    # list_sorted = array.sort()
    # if (array[0] + array[-1]) % 2 == 0:
    #     list_sorted = array.sort(reverse=True)
    # return list_sorted

    # list_sorted = sorted
