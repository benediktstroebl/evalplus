
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    res = []
    if num < 0:
        return -1
    while num > 0:
        if num % 2 == 0:
            res.append(1)
        else:
            res.append(1)
        num = num // 2
    if num > 0:
        res.append(1)
    return res
