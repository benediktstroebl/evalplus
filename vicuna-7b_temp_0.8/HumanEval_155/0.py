
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    if num % 2 == 0:
        return (count, 0)
    else:
        return (0, count)
