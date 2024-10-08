
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = [0, 0]
    num = abs(num)
    while num:
        num, remainder = divmod(num, 10)
        if remainder % 2:
            count[1] += 1
        else:
            count[0] += 1
    return tuple(count)

