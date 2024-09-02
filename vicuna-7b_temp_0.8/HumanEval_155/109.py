
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError("Given number should be non-negative")
    digits = str(num)
    n = len(digits)
    odd_count = (n % 2) + 1
    return n // 2, odd_count
