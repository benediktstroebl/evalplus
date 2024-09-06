
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    counter = 0
    result = [0, 0]
    if num < 0:
        num = -num

    while num > 0:
        num, remainder = divmod(num, 10)
        if remainder % 2 == 0:
            result[0] += 1
        else:
            result[1] += 1
    return tuple(result)

