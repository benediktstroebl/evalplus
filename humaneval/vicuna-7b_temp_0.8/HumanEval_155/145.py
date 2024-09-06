
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    return sum(1 for i, c in enumerate(digits) if c in '02468') % 2, sum(1 for i, c in enumerate(digits) if c in '13579') % 2
