
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return(0, 0)
    if num < 0:
        num = abs(num)
    if num == 1:
        return(0, 1)
    is_even = num%2 == 0
    if is_even:
        return(0, 0)
    else:
        return(1, 1)

