
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    return sum(map(int, str(abs(num))[:2]) + [0, 1]), sum(map(int, str(abs(num))[-2:]))

