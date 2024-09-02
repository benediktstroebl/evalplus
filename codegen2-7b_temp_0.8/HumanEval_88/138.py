
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
    if array:
        sorted_array = []
        temp = []
        for i in array:
            if len(sorted_array) == 0:
                temp.append(i)
            elif sorted_array[-1] < i:
                temp.append(i)
                sorted_array.append(i)
            else:
                temp.append(i)
        return temp + sorted_array
    else:
        
