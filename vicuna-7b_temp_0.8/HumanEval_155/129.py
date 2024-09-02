
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # if the number is negative, return (0, 0)
    if num < 0:
        return (0, 0)
    # else, convert the number to a string and split it into a list of digits
    digits = str(num).split('')
    # initialize an empty list for the number of even digits
    even_digits = []
    # iterate over the digits in the list
    for digit in digits:
        # if the digit is even, append it to the even_digits list
        if digit % 2 == 0:
            even_digits.append(digit)
    # if the number of even digits is odd, return (0, 1)
    if len(even_digits) % 2 == 1:
        return (0, 1)
    else:
        # otherwise, return the number of even and odd digits
        return len(even_digits), len(digits) - len(even_digits)
