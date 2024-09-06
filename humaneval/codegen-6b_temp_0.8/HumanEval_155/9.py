
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    evens = 0
    odds = 0
    num_abs = abs(num)
    while num_abs > 0:
        if num_abs % 2 == 0:
            evens += 1
        else:
            odds += 1
        num_abs = num_abs // 10
    return (evens, odds)

