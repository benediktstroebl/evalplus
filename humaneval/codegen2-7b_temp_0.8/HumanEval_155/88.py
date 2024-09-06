
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_odd = 0
    while num > 0:
        odd, rem = divmod(num, 10)
        even, rem = divmod(rem, 2)
        even_odd += even + odd
        num = odd
    return even_odd, even_
