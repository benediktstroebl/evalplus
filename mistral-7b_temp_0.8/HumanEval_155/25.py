
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num < 0:
        num = -num

    num_even_digits = 0
    num_odd_digits = 0
    while num:
        last_digit = num % 10
        num = num // 10

        if last_digit % 2 == 0:
            num_even_digits += 1
        else:
            num_odd_digits += 1

    return (num_even_digits, num_odd_digits)
