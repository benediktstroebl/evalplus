
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    c = 0
    while num:
        num = num // 10
        c += 1
    if c % 2 == 0:
        return (c // 2, c // 2)
    return (c // 2 + 1, c // 2)
