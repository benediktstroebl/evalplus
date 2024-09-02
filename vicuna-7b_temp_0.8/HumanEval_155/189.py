
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError("Cannot get digits of negative number")
    digits = str(num)
    odd_count = sum(1 for d in digits if d.isdigit() and d % 2 == 1)
    even_count = sum(1 for d in digits if d.isdigit() and d % 2 == 0)
    return (odd_count, even_count)
