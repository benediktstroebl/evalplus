
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digit_count = 0
    odd = False
    for d in str(num):
        if odd:
            digit_count += 1
        if not odd:
            odd = True
    return digit_count, digit_count
