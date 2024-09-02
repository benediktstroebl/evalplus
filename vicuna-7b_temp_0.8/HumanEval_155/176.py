
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = int(num)
    if num < 0:
        return -1, 0
    if num == 0:
        return 0, 0
    if num == 1:
        return 1, 0
    elif num % 2 == 0:
        return 0, 1
    else:
        return 1, 1
