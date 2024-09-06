
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Use bitwise and operator '&' to check if the last digit is zero
    if num % 10 == 0:
        return 0, 0
    else:
        # If the last digit is not zero, then we have an odd number
        return 1, 1
