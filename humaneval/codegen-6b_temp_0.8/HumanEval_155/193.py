
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    result = []
    for n in [int(x) for x in str(abs(num))]:
        if n % 2 == 0:
            result.append(1)
        else:
            result.append(0)
    return tuple(result)
