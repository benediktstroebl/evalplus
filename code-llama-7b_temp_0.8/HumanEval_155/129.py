
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    #return ((num + 1) / 2, (num + 1) / 2)

    even = num // 2
    odd = num // 2 + 1

    return (even, odd)

