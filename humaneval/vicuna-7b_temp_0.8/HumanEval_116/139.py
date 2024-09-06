
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # Check if the array is empty
    if not arr:
        return []

    # Initialize a variable to store the index of the element in the new array
    count = 0

    # Iterate through the array
    for i in range(len(arr)):
        # Get the binary representation of the element
        binary = bin(arr[i])

        # Find the index of the first 1 in the binary representation
        index = binary.find('1')

        # Increment the count variable
        count += index + 1

    # Initialize a new array with the sorted elements
    sorted_array = []

    while count > 0:
        # Divide the count by 2 to find the next index of 1 in the binary representation
        next_index = count // 2

        # Append the current element to the sorted array
        sorted_array.append(arr[i])

        # Decrement the count variable
        count = count // 2

    # Append the remaining elements to the sorted array
    sorted_array.extend(arr[i:])

    return sorted_array