
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    sign = 1 if num < 0 else 0
    n = abs(num)
    res = 0
    while n:
        n = int(n / 10)
        res += sign * n % 2
    return res
