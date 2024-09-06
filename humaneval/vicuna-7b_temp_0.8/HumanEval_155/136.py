
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    n = len(digits)
    if n % 2 == 0:
        return n // 2, n // 2
    else:
        return n, n - 1
