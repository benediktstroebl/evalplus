
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    odd_count = 0
    for digit in digits:
        if digit in "0123456789":
            odd_count += 1
    return odd_count, len(digits) - odd_count
