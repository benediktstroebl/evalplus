
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
    # create a new array to store the sorted array
    # if the sum of elements in the original array is odd,
    # the last element in the new array will be the largest number
    # if the sum of elements in the original array is even,
    # the first element in the new array will be the smallest number
    sorted_array = []

    # iterate through the original array
    for i in range(len(array)):
        # if the sum of the first element and the last element of the original array is odd,
        # the current element is the largest number in the original array
        # and it should be the first element in the sorted array
        if (array[i] + array[i+1]) % 2 == 1:
            sorted_array.insert(0, array[i])
        # if the sum of the first element and the last element of the original array is even,
        # the current element is the smallest number in the original array
        # and it should be the last element in the sorted array
        elif (array[i] + array[i+1]) % 2 == 0:
            sorted_array.append(array[i])
        else:
            sorted_array.append(array[i])
            
    return sorted_array