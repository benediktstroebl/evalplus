
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # return a tuple of the number of even and odd digits respectively
    digits = str(num)
    if digits[0] % 2 == 0:
        evens = 0
    else:
        evens = 1
    if digits[1] % 2 == 0:
        odds = 0
    else:
        odds = 1
    return (evens, odds)
