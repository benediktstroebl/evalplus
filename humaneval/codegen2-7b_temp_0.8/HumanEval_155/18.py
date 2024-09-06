
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = num * -1
    num = str(num)
    even = len(num) - num.count('0')
    odd = num.count('0')
    return (even, odd)

