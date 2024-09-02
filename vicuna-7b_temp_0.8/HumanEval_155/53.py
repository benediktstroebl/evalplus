
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    d = num // 10
    n = num % 10
    if n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return d, n-d
    else:
        return d, n-d+1
