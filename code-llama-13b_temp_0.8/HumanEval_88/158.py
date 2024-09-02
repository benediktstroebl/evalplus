
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
    # 0. Check if the array is empty or has only 1 element
    # 1. Sort the array with default sorting algorithm
    # 2. Create a variable to check if the array is even or odd
    # 3. Create a variable to store the sorted array
    # 4. Iterate over the array
    # 5. Check if the array is even or odd
    # 6. If the array is even, insert to the front of the sorted array
    # 7. If the array is odd, insert to the back of the sorted array
    # 8. Return the sorted array

    # 0. Check if the array is empty or has only 1 element
    if not array or len(array) == 1:
        return array

    # 1. Sort the array with default sorting algorithm
    sorted_array = sorted(array)

    # 2. Create a variable to check if the array is even or odd
    array_is_even = sum(array[0], array[-1]) % 2 == 0

    # 3. Create a variable to store the sorted array
    sorted_array = []

    # 4. Iterate over the array
    for element in array:
        # 5. Check if the array is even or odd
        if array_is_even:
            # 6. If the array is even, insert to the front of the sorted array
            sorted_array.insert(0, element)
        else:
            # 7. If the array is odd, insert to the back of the sorted array
            sorted_array.append(element)

    # 8. Return the sorted array
    return sorted_array

