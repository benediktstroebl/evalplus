
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    negative = False
    if num < 0:
        negative = True
        num *= -1
    if num == 0:
        return (1, 0) if negative else (0, 1)
    even_cnt = 0
    odd_cnt = 0
    while num > 0:
        if num % 10 % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
        num //= 10
    return (even_cnt, odd_cnt) if not negative else (-even_cnt, -odd_cnt)

