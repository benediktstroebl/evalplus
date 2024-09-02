
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    e, o = 0, 0
    while num > 0:
        d = num % 10
        if d % 2 == 0:
            e += 1
        else:
            o += 1
        num //= 10

    return (e, o)
