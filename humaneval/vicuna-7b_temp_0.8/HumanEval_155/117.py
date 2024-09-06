
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    sign = 1
    if num < 0:
        count, sign = -1, -1
        num = abs(num)
    while num != 0:
        count += sign * int(num % 10)
        sign *= 10
        num //= 10
    return (count % 2 == 0, count // 2)
