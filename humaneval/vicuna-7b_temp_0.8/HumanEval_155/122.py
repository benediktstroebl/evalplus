
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1

    result = []
    for i in range(len(str(num))):
        if str(num)[i] in '01':
            result.append(result[-1] or 0)
        else:
            result.append(1)
    return result
