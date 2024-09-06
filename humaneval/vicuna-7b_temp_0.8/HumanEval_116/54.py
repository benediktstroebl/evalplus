
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
    # Aux function to get the number of ones in the binary representation
    def get_num_of_ones(num):
        """
        Return the number of ones in the binary representation of the number
        """
        # Check if the number is negative
        if num < 0:
            return 1 + get_num_of_ones(-num)
        # Get the binary representation of the number
        bin = str(num)
        # Get the number of digits in the binary representation
        num_of_digits = len(bin)
        # Check if the number is 0 or 1
        if not bin:
            return 0
        # Check if the first digit is 1
        if bin[0] == '1':
            return 1
        # Return the number of ones
        return num_of_digits - 1

    # Sort the array
    sorted_arr = sorted(arr, key=lambda x: get_num_of_ones(int(x)))

    return sorted_arr