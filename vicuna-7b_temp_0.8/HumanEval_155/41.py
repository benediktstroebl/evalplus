
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    n_even = 0
    n_odd = 0
    for d in digits:
        if d % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    return n_even, n_odd
