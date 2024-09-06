
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []
    for num in range(a, b+1):
        str_num = str(num)
        if len(str_num) == 1:
            if str_num == '0':
                continue
            if int(str_num) % 2 == 0:
                even_digits.append(num)
        else:
            even = True
            for digit in str_num:
                if int(digit) % 2 != 0:
                    even = False
                    break
            if even:
                even_digits.append(num)
    return even_digits
