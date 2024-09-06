
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_digits = 0
    odd_digits = 0
    while num > 0:
        remainder = num % 10
        if remainder % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        num = num // 10
    return even_digits, odd_digits

