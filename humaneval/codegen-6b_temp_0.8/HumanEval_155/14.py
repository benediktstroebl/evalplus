
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (1, 0)

    sign = -1 if num < 0 else 1
    num = abs(num)
    even_digits = 0
    odd_digits = 0
    while num != 0:
        digit = num % 10
        num //= 10
        if sign * digit % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
    return (even_digits, odd_digits)
