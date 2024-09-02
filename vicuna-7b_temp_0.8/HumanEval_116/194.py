
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
    def count_ones(num):
        """
        Return the number of ones in the binary representation of a number.
        """
        count = 0
        while num > 0:
            if num % 2 == 0:
                count += 1
                num //= 2
            else:
                num -= 1
        return count

    def binary_to_decimal(num):
        """
        Convert a number in binary form to decimal form.
        """
        return sum(num >> i * 2**i for i in range(0, len(num), 1))

    def compare(a, b):
        if count_ones(binary_to_decimal(a)) == count_ones(binary_to_decimal(b)):
            return cmp(a, b)
        return count_ones(binary_to_decimal(a)) > count_ones(binary_to_decimal(b))

    return sorted(arr, key=compare)
