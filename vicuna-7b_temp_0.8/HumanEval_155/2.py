
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1, 0
    else:
        digits = []
        for d in str(num):
            digits.append(d % 10)
        return 0, len(digits) % 2
