
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, -1)
    elif num == 0:
        return (0, 0)
    elif not num % 2:
        return (1, 1)
    else:
        return (1, 0)
