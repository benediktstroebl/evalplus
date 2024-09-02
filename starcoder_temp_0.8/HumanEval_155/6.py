
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num *= -1
    cnt_even = 0
    cnt_odd = 0
    while num:
        if num % 10 % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1
        num //= 10
    return cnt_even, cnt_odd

