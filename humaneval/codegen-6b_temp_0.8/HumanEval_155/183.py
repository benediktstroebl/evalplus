
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    odd_count = long(num % 10)   # the last digit
    even_count = long(num / 10)  # the rest of the digits
    return (even_count, odd_count)
