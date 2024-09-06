
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # convert the input string to a number
    n = int(str(num))
    # check if the number is even or odd
    if n % 2 == 0:
        # if the number is even, the number of even digits is the number of digits
        return (n // 2, n // 2)
    else:
        # if the number is odd, the number of odd digits is 1 less than the number of digits
        # and the number of even digits is the number of digits minus 1
        return (n, n - 1)
