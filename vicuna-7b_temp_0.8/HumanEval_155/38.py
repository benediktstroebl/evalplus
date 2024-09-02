
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    sign = '-' if num < 0 else '+'
    num_str = sign + str(abs(num))
    return num_str[::2], num_str[1::2]
