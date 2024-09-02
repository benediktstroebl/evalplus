
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # handle the case when the input is negative
    if num < 0:
        return (int(num/2), int(-num%2))
    else:
        return (int(num/2), int(num%2))
