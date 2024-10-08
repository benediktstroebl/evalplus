
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    negative = False
    if num < 0:
        negative = True
        num = num * -1
    while num:
        if num % 10 % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    if negative:
        even_count, odd_count = odd_count, even_count
    return (even_count, odd_count)
