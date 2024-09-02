
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if isinstance(num, float):
        return (0, 0)
    else:
        return (len(str(num)), len(str(num).replace("-", "")))
