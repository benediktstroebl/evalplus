
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
    #you cannot sort the given array because that would make it impossible to return the value you want
    #create a new array and sort that

    new_array = []
    odd_even = array[0] + array[-1]
    if odd_even % 2 == 0:
        #sort the array
        new_array = sorted(array, reverse=True)
    else:
        new_array = sorted(array)
    return new_array


