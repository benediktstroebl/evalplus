
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    sign = 1 if num < 0 else 0
    num = abs(num)
    if num < 10:
        return sign, 1
    while True:
        if num % 10 == 0:
            return sign*2, num // 10
        num /= 10
    return sign, 0