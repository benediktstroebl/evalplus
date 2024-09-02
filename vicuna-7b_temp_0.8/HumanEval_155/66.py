
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # This is a common way to check if the number is even or odd
    # i.e. it has an odd number of digits or an even number of digits
    # if it has an odd number of digits, the last digit must be odd
    # if it has an even number of digits, the last digit must be even
    return num // 2, (num // 2) % 2
