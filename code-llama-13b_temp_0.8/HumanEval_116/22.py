
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

    # Step 1: create a list of tuples of (num, # of ones)
    arr_tuples = [(num, bin(num).count('1')) for num in arr]

    # Step 2: Sort on the tuple on (# of ones, num)
    arr_tuples.sort(key=lambda x: (x[1], x[0]))

    # Step 3: Return a list of sorted nums
    return [num for num, ones in arr_tuples]

