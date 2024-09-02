
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digit_list = list(str(num))
    if len(digit_list) % 2 == 0:
        return (int(digit_list[::2]), int(digit_list[1::2]))
    else:
        return (int(digit_list[1::2]), int(digit_list[::2]))
