
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    i = 10
    result = []
    while i >= 0:
        if num % i == 0:
            result.append(i)
        i -= 1
    return result

