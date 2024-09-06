
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    elif not str(num).startswith('-'):
        result = 0
        n = 0
        while num > 0:
            n += 1
            result, num = divmod(num, 10)
        result += n // 2
        return result, n % 2
    else:
        return -1
