
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)
    even_count = odd_count = 0
    if num == 0:
        return (1, 0)
    while num:
        if num & 1:
            odd_count += 1
        else:
            even_count += 1
        num >>= 1
    return even_count, odd_count

