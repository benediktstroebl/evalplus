
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # a string is a sequence of characters
    str_num = str(num)
    # find the number of digits in the number
    n = len(str_num)
    # if the number is negative, the number of odd digits will be zero
    if num < 0:
        evens = 0
        odds = n
    else:
        evens = n // 2
        odds = n % 2
    # return the number of even and odd digits
    return (evens, odds)