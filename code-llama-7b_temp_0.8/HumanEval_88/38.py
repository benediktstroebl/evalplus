
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
    #initialize variables
    result = []
    smallest = None
    largest = None
    #check if array length is zero
    if len(array) == 0:
        return []
    #check if sum of first and last index is odd
    if sum(array[0], array[-1]) % 2 == 1:
        smallest = array[-1]
        largest = array[0]
    #check if sum of first and last index is even
    elif sum(array[0], array[-1]) % 2 == 0:
        smallest = array[0]
        largest = array[-1]
    #loop through the array
    for i in array:
        #if number is smaller than largest
        if i < largest:
            #make number smaller
            array[array.index(i)] = array[array.index(i)] + 1
            #add number to result
            result.append(array[array.index(i)])
        #if number is larger than smallest
        elif i > smallest:
            #make number larger
            array[array.index(i)] = array[array.index(i)] - 1
            #add number to result
            result.append(array[array.index(i)])
        #if number is equal to largest or smallest
        else:
            #add number to result
            result.append(array[array.index(i)])

    return result
