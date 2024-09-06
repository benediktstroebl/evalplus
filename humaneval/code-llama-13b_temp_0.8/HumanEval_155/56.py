
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (1, 0)
    elif num < 0:
        num = abs(num)
        if num % 2:
            return (0, 1)
        else:
            return (1, 1)
    else:
        if num % 2:
            return (1, 1)
        else:
            return (1, 0)

    """
    if num == 0:
        return (1, 0)
    if num < 0:
        num = abs(num)
    s = str(num)
    return (sum(int(c) % 2 == 0 for c in s), sum(int(c) % 2 == 1 for c in s))
    """

