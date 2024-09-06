
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-num, 0)
    elif num == 0:
        return (0, 0)
    else:
        digits = str(num)
        evens = 0
        odds = 0
        for d in digits:
            evens += d.isdigit() % 2 == 0
            odds += d.isdigit() % 2 == 1
        return (evens, odds)
