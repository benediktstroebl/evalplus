
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
    # task:
    # Given an array of non-negative integers, return a copy of the given array after sorting,
    # you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    # or sort it in descending order if the sum( first index value, last index value) is even.

    # Example:
    # sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    # sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]

    # make a copy of the given array
    # we need to check the sum( first index value, last index value) is odd or even
    # if odd then sort in ascending order
    # if even then sort in descending order
    # sort the copy of the array
    # return the sorted copy

    array_copy = []
    for num in array:
        array_copy.append(num)
    print(array_copy)

    sum_of_first_and_last_values = array_copy[0] + array_copy[-1]
    print(sum_of_first_and_last_values)

    if sum_of_first_and_last_values % 2 == 1:
        print("odd")
        array_copy = sorted(array_copy)
    else:
        print("even")
        array_copy = sorted(array_copy, reverse=True)

    return array_copy

