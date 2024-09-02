
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    even = odd = 0
    while num:
        even += num & 1 == 0
        odd += num & 1
        num >>= 1
    return (even, odd)
