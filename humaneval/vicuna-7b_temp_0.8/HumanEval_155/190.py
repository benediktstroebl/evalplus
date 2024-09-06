
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = int(num)
    if num < 0:
        return (-num, 0)
    if num == 0:
        return (0, 1)
    n = 1
    d = 1
    while True:
        d *= 10
        n *= 10
        if d > 9 and (num / d) % 2 == 0:
            n += 1
        elif d > 9 and (num / d) % 2 == 1:
            n -= 1
        else:
            break
    return (n, d)
