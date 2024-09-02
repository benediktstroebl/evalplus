
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    list_num = []
    num = x
    while num > 0:
        list_num.append(num % 10)
        num = num // 10

    list_num = list_num[:len(list_num) - shift] + list_num[len(list_num) - shift:]
    new_list = []
    for num in list_num:
        new_list.append(str(num))
    return "".join(new_list)

