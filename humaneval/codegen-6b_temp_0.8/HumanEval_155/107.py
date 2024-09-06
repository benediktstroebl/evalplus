
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    n_abs = abs(num)
    while True:
        if n_abs == 0:
            break
        digit = n_abs % 10
        if digit % 2 == 0:
            even_count += 1
            n_abs //= 10
        else:
            odd_count += 1
            n_abs //= 10
    return (even_count, odd_count)

