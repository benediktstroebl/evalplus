
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    n = len(str(abs(num)))
    if n == 1:
        return (0, 1)
    else:
        e = sum([int(d) % 2 for d in str(num)])
        o = n - e
        return (e, o)
