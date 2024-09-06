
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
    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        return arr[0]
    else:
        n_ones = 0
        last_digit = 0
        for i in arr:
            last_digit = int(str(i)[-1])
            n_ones += last_digit
        # sort based on number of ones
        result = []
        for i in range(n_ones, 0, -1):
            result.append(arr[i])
        # add the last digit if it is greater than the previous digit
        if last_digit > n_ones:
            result.append(arr[n_ones])
        return result
