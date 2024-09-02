
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
    # Convert the input list of integers to a list of tuples where the tuple
    # contains the original integer and a '1' or '0' indicating the number of
    # ones in the binary representation of the integer.
    num_tuples = [(int(i), '0' if i < 10 else '1') for i in arr]

    # Sort the tuples based on the number of ones in the binary representation
    num_tuples_count = {}
    for i, (num, _):
        if num not in num_tuples_count:
            num_tuples_count[num] = 1
        else:
            num_tuples_count[num] += 1

    num_tuples_sorted = sorted(num_tuples_count.items(), key=lambda x: x[1], reverse=True)

    # Convert the sorted list of tuples back to a list of integers
    return [i[0] for i in num_tuples_sorted]
