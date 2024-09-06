
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
    # Get the length of the array
    n = len(arr)

    # Initialize a variable to store the current index
    i = 0

    # Create a variable to store the array in its sorted form
    sorted_arr = [0] * n

    # Loop through the array
    for num in arr:
        # Get the binary representation of the number
        binary = bin(num)[2:]
        # Get the number of digits in the binary representation
        digits = len(binary)
        # If the number of digits is zero, put the number in the sorted array at index 0
        if digits == 0:
            sorted_arr[0] = num
        # If the number of digits is one, put the number in the sorted array at index 1
        elif digits == 1:
            sorted_arr[1] = num
        # If the number of digits is greater than one, put the number in the sorted array at index 1
        else:
            # Get the decimal value of the number
            decimal = num
            # Compare the number with the numbers in the sorted array
            # The current number is greater than the sorted array, so
            # increment the current index and continue with the next number
            while i < n and sorted_arr[i] < decimal:
                sorted_arr[i] += 1
                i += 1
            # Put the current number in the sorted array at the current index
            sorted_arr[i] = decimal

    return sorted_arr