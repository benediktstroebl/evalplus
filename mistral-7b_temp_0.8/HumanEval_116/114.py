
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

    sorted_list = []
    for number in arr:
        if len(sorted_list) == 0:
            sorted_list.append(number)
            continue
        elif len(sorted_list) > 0:
            if len(str(bin(number)).replace("0b", "")) < len(str(bin(sorted_list[-1])).replace("0b", "")):
                sorted_list.append(number)
                continue
            elif len(str(bin(number)).replace("0b", "")) == len(str(bin(sorted_list[-1])).replace("0b", "")):
                if number > sorted_list[-1]:
                    sorted_list.append(number)
                    continue
                else:
                    continue
    return sorted_list


