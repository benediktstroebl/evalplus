
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num *= -1

    n_digits = 0
    odd_digits = 0

    while num > 0:
        num, n_digits = num // 10, n_digits + 1
        digit = num % 10

        if digit % 2 == 1:
            odd_digits += 1

    return n_digits, odd_digits
