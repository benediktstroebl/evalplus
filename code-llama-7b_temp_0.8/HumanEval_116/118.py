
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

    # Define the odd and even groups
    odds = list(filter(lambda x: x & 1 == 1, arr))
    evens = list(filter(lambda x: x & 1 == 0, arr))

    # Get the number of 1s in each group
    odds = sorted(odds, key=lambda x: bin(x).count("1"), reverse=True)
    evens = sorted(evens, key=lambda x: bin(x).count("1"), reverse=True)

    # Recombine the list
    return (odds + evens)
