
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # check if the input is negative
    if num < 0:
        return str(abs(num)).split('').count('0'), str(abs(num)).split('').count('1')
    else:
        return str(num).count('0'), str(num).count('1')
