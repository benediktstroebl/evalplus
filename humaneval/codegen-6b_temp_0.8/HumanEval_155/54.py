
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return 0
    else:
        if num < 0:
            return even_odd_count(-num)
        digits = len(str(abs(num)))
        return (digits - len(str(abs(num)).split('0')[1])), (digits - len(str(abs(num))[::-1].split('0')[1]))

