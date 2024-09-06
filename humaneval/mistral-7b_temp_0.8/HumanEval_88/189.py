
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
    # given array:
    # - if first index + last index is odd
    # - sort in ascending order
    # - if first index + last index is even
    # - sort in descending order

    # - first index value
    # - last index value

    # create a new array
    new_array = []
    # for loop over the array
    # - check the sum of the first and last index value
    # - if the sum is even:
    # - sort in descending order
    # - if the sum is odd:
    # - sort in ascending order
    # - add the sorted values to the new array

    # return the new array

    for index, value in enumerate(array):
        if index == 0:
            # return new_array
            new_array.append(array[index])
        elif index == len(array) - 1:
            new_array.append(array[index])
            new_array = sorted(new_array, reverse=True)
        elif len(array) % 2 == 1:
            new_
