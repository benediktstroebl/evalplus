```python
def sort_array(arr):
    """
    Sorts the array of integers with non-negative values according to the number of ones in their binary representation.

    Args:
        arr (list): Array of integers with non-negative values.

    Returns:
        sorted array of integers with non-negative values in ascending order.
    """

# Binary representation of numbers:
# Each digit is either 0, 1, or 2. The most significant digit represents the binary value,
# and the others are 'don't matter'.

    def binary(number):
        """
        Returns the binary representation of the number.
        Args:
        number (int): Integer to be represented in binary.
        """
        # Initialize the a counter for the most significant digit
        counter = 0
        """
        return bin(number)[2:]

    def count_ones(binary):
        """
        Count the number of ones in the binary representation.

        Args:
        binary (strng): Binary representation of an integer

        Returns:
        count (int): Number of ones in the binary representation of the integer
        """
        return sum(1 for bit in binary if bit == '1')

    arr = [1, 5, 2, 3, 4]
    sorted_arr = sorted(arr, key=count_ones)
    return sorted_arr
```