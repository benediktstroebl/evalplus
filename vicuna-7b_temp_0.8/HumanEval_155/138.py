
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    n = int(num)
    res = []
    while n > 0:
        if n % 2 == 0:
            res.append(n % 2)
            n = n // 2
        else:
            res.append(1)
            n = n // 2
    return res
