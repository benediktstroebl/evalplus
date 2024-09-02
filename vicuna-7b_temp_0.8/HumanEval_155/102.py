
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    if digits.endswith("0"):
        digits = digits[:-1]
    return sum(1 for digit in digits if digit in "02468"), sum(1 for digit in digits if digit not in "02468")
