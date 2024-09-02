
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_e = 0
    count_o = 0
    num_abs = abs(num)
    while num_abs > 0:
        if num_abs % 10 % 2 == 0:
            count_e += 1
        else:
            count_o += 1
        num_abs //= 10
    return (count_e, count_o)



