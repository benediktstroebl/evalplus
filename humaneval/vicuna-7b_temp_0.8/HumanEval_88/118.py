
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
    # Keep track of the number of odd and even elements in the array
    odd_count = 0
    even_count = 0

    # Loop through the array and count the number of odd and even elements
    for num in array:
        odd_count += (num % 2 == 0)
        even_count += (num % 2 == 1)

    # If the number of odd and even elements is the same, return the array as is
    if odd_count == even_count:
        return array

    # If the number of odd and even elements is not the same, return a sorted copy of the array
    return array[::-1] if odd_count % 2 == 0 else array[::-1][:even_count] + array[even_count::]