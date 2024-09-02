
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
    # do not forget to start with an empty array, not with None!
    result = []

    for n in arr:
        # convert n to binary representation (reverse order)
        # n=1 becomes '1' and n=2 becomes '10'
        # then, add 0 to binary until number of digits is even
        binary = bin(n).replace('0b', '')[::-1]
        while len(binary) % 2 == 1:
            binary = binary + '0'
        # create a string of '01'
        # n=1 becomes '01' and n=2 becomes '0101'
        z = binary.replace('0', '01').replace('1', '10')
        # join the strings with no delimiter
        # n=1 becomes '01' and n=2 becomes '0101'
        # then convert back to int (reverse order)
        result.append(int(z[::-1]))

    return sorted(result)

