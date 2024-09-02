
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = sum(1 for c in str(num) if c.isdigit() and int(c) % 2 == 0)
    odd = sum(1 for c in str(num) if c.isdigit() and int(c) % 2 == 1)
    return (even, odd)
