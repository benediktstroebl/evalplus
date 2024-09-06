
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # ring = {
    #     1: "I",
    #     5: "V",
    #     10: "X",
    #     50: "L",
    #     100: "C",
    #     500: "D",
    #     1000: "M"
    # }
    ring = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m"
    }
    result = ""
    i = 0
    while number:
        digit = number % 10
        if digit == 0:
            pass
        elif digit <= 3 and ring[10**i] == ring[10**(i-1)]:
            result = ring[10**(i-1)] + ring[10**i] * digit + result
        elif digit == 4:
            result = ring[10**(i-1)] + ring[10**i] + result
        elif digit <= 8 and ring[10**i] == ring[10**(i-1)]:
            result = ring[10**i] + ring[10**(i-1)] * (digit-5) + result
        elif digit == 9:
            result = ring[10**(i-1)] + ring[10**i] + ring[10**(i-1)] + result
        else:
            result = ring[10**i] * digit + result
        number = number // 10
        i += 1
    return result

