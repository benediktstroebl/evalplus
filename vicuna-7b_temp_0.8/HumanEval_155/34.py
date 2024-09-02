
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    if digits[-1] in "0":
        digits = digits[:-1]
    if digits.isdigit()[-1]:
        digits = digits[:-1]
    return int(digits), int(digits[-1])
