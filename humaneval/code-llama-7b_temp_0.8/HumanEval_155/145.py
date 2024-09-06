
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    result = tuple()
    even = 0
    odd = 0
    for c in str(num):
        if c.isdigit():
            if int(c) % 2 == 0:
                even += 1
            else:
                odd += 1
    result = (even, odd)
    return result
