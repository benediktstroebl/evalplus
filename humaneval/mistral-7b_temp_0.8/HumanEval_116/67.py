
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
    # So first, a new list is created that contains the list of binary representations of each element in arr
    # Each element is checked to see if it is positive or negative, if positive, then its binary representation is converted to a string
    # if negative, then its absolute value is converted to a string
    # The integer is then converted to a binary representation
    # Each element in arr is checked to see if it is positive or negative
    # If positive, then the element is divided by 2 and its modulus is added to the list, this is done until 0 is reached
    # If negative, then the absolute value is divided by 2 and its modulus is added to the list, this is done until 0 is reached
    # The list is sorted in ascending order
    # The sorted list is then converted to a binary representation
    # The decimal value is then returned
    return sorted(map(lambda x: bin(abs(x))[2:],arr))


