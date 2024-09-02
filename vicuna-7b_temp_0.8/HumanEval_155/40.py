
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = int(num)
    if num < 0:
        return -1
    if not num % 10:
        return (1, 0)
    count = 0
    while num:
        count += 1
        num = num // 10
    return (count % 2, 1) + (count / 2)
