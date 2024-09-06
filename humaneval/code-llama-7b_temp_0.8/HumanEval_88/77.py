
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
    # The idea is to create a new list and start adding elements in it.
    # We will iterate through the given list.
    # If the sum of first and last index element is odd then we will add the smallest element to the new list.
    # Else, we will add the largest element to the new list.
    # O(n) time | O(n) space - where n is the length of the input array.
    def get_smallest_element_index(array):
        smallest_element_index = 0
        for i in range(1, len(array)):
            if array[i] < array[smallest_element_index]:
                smallest_element_index = i
        return smallest_element_index

    def get_largest_element_index(array):
        largest_element_index = 0
        for i in range(1, len(array)):
            if array[i] > array[largest_element_index]:
                largest_element_index = i
        return largest_element_index

    new_array = []
    if len(array) == 0:
        return new_array
    sum_of_first_and_last_element = array[0] + array[-1]
    if sum_of_first_and_last_element % 2 == 0:
        new_array.append(array[0])
        for i in range(1, len(array) - 1):
            if array[i] > array[i + 1]:
                new_array.append(array[i + 1])
            else:
                new_array.append(array[i])
        new_array.append(array[-1])
    else:
        new_array.append(array[-1])
        for i in range(len(array) - 2, -1, -1):
            if array[i] > array[i + 1]:
                new_array.append(array[i])
            else:
                new_array.append(array[i + 1])
        new_array.append(array[0])
    return new_array







