
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    c_even, c_odd = 0, 0

    if num < 0:
        num *= -1

    while num > 0:
        if num % 2 == 0:
            c_even += 1
        else:
            c_odd += 1
        num //= 10

    return (c_even, c_odd)

