
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    str_num = str(num)
    for c in str_num:
        if c in ["0", "2", "4", "6", "8"]:
            even += 1
        else:
            odd += 1
    return (even, odd)

