
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    if num < 0:
        raise ValueError('Cannot return the number of digits of a negative number.')

    if num < 10:
        return (num, 0)
    else:
        for i in range(1, num + 1):
            if i % 2 == 0:
                even +=
