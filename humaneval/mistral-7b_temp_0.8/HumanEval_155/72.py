
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    e = 0
    o = 0

    if num < 0:
        num *= -1

    while num:
        if num % 10 % 2 == 0:
            e += 1
        else:
            o += 1

        num //= 10

    return e, o

