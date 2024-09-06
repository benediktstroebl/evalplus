
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (0, 0)
    else:
        if num%2 == 0:
            return (num/2, even_odd_count(num/2)[1])
        else:
            return (num/2+1, even_odd_count(num/2)[1]+1)
