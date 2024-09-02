
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num > 0:
        even = len([i for i in str(num) if int(i) % 2 == 0])
        odd = len([i for i in str(num) if int(i) % 2!= 0])
        return (even, odd)
    if num < 0:
        num = abs(num)
        even = len([i for i in str(num) if int(i) % 2 == 0])
        odd = len([i for i in str(num) if int(i) % 2!= 0])
        return (even, odd)
    else:
        return (0, 0)

