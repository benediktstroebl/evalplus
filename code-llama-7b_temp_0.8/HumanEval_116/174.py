
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
    list_of_ones = []
    list_of_others = []
    # higher_bit is the higher bit that needs to be added.
    higher_bit = 1
    for number in arr:
        # Check for ones in binary representation of each number.
        count = 0
        while number > 0:
            if number & higher_bit:
                count += 1
            number = number << 1
        if count > 0:
            # Add number to list_of_ones.
            list_of_ones.append((count, number))
        else:
            # Add number to list_of_others.
            list_of_others.append(number)
    # Sort list_of_ones and list_of_others in ascending order.
    list_of_ones.sort()
    list_of_others.sort()
    result = list_of_ones[:]
    result.extend(list_of_others)
    return result

