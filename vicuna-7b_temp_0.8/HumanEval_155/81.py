
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = [int(d) for d in str(num)]
    if sum(digits) % 2 == 0:
        return digits[:1], digits
    else:
        return digits[:-1], digits[-1]
