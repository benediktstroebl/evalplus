
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
    one_matches = defaultdict(list)

    for num in arr:
        num_bin_rep = bin(num)
        num_bin_rep = num_bin_rep.replace("-", "")
        num_bin_rep = num_bin_rep.replace("0b", "")
        num_bin_rep = num_bin_rep.replace("-", "")
        one_count = num_bin_rep.count("1")
        one_matches[one_count].append(num)

    return sorted(one_matches.values(), key=lambda x: sorted(x))

