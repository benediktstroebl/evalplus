

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    x_list = list(str(x))
    x_list.reverse()
    num_list = [int(str(x)) for x in x_list]
    # print(num_list)
    ans_list = []
    while num_list:
        if sum(num_list) >= base:
            carry = sum(num_list) // base
            ans_list.append(sum(num_list) % base)
            num_list = num_list[:-1]
            ans_list.append(carry)
        else:
            ans_list.append(sum(num_list))
            num_list = num_list[:-1]
    return ''.join([str(i) for i in ans_list[::-1]])

