
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    is_even = num % 2 == 0
    is_odd = not is_even
    return (num // 10, is_even, is_odd
