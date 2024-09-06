
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = -num
        n = 1
    else:
        n = 0
    while num // 10:
        if num % 10 % 2 == n:
            n += 1
        num //= 10
    return (n, num % 10)
