
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    # count = 0
    # for element in arr:
    #     ele_as_string = str(element)
    #     ele_as_list = list(ele_as_string)
    #     digits_as_int = []
    #     for char in ele_as_list:
    #         if char != "-":
    #             digits_as_int.append(int(char))
    #     sum = 0
    #     for digit in digits_as_int:
    #         sum += digit
    #     if sum > 0:
    #         count += 1
    # return count

    return len([x for x in arr if sum(map(int, str(x))) > 0])

