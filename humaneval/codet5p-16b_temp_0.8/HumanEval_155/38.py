
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num == 0:
        return (0, 0)

    even = 0
    odd = 0

    while num:
        num, d = divmod(num, 10)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)
