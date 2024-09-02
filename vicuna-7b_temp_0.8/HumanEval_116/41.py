
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
    # Sort the array
    sorted_arr = sorted(arr)

    # Create an empty list to store the result
    result = []

    # Create a variable to keep track of the current position
    current_position = 0

    # Iterate over the sorted array
    for i in range(len(sorted_arr)):
        # Check if the number at the current position has one in its binary representation
        has_one = any(x == 1 for x in sorted_arr[current_position:])

        # If it does, increment the current position
        if has_one:
            current_position += 1
        else:
            # If not, add the current element to the result list
            result.append(sorted_arr[current_position])
            # Remove the current element from the sorted array
            sorted_arr.pop(current_position)

            # Update the current position to the end of the array
            current_position = len(sorted_arr)

    # Add the remaining elements to the result list
    result.extend(sorted_arr)

    return result