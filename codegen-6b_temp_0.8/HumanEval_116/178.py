
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
    def dec_to_bin(num):
        return '{:b}'.format(num)

    def bin_to_dec(num):
        return int(num, 2)

    def length(num):
        return len(num)

    def sort_key(key):
        return bin_to_dec(key)

    def bin_num_of_ones(num):
        results = []

        for char in dec_to_bin(num):
            results.append(char)

        return results.count('1')

    return sorted(arr, key=sort_key, reverse=False)



