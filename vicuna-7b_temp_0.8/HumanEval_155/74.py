
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # base case
    if num == 0:
        return (0, 0)
    # get the digit as string
    str_num = str(num)
    # get the length of the string
    str_len = len(str_num)
    # get the number of digits
    num_digits = int(log10(num))
    # check if the number is positive or negative
    if num > 0:
        # if the number is even, return the number of digits
        return (num_digits, num_digits)
    else:
        # if the number is odd, the number of odd digits is equal to the number of digits
        # minus one, and the number of even digits is 0
        return (num_digits - 1, 0)
