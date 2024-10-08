
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    return tuple(len([x for x in str(num) if int(x) % 2 == 0]) for num in [num, num*-1])
