
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    evens = 0
    odds = 0
    for x in str(num):
        if x in ('0', '2', '4', '6', '8'):
            evens += 1
        else:
            odds += 1
    return (evens, odds)

