
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = []
    for i in xrange(1, num+1):
        if (i < 10):
            digits.append(i)
        elif (i % 2 == 0):
            digits.append(0)
        else:
            digits.append(1)
    return (digits.count(0), digits.count(1))
