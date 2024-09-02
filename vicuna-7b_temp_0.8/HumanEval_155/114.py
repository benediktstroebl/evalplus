
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    sign = num / 2
    num = int(num)
    if num % 2 == 0:
        return sign, 1
    else:
        return sign, 0
