
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    odd, even = 0, 0
    while num:
        odd, even = even + num % 10, odd + (num % 10)
        num //= 10
    return odd,
