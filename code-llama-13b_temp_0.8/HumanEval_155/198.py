
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if isinstance(num, int) == False:
        raise ValueError("{0} is not an integer.".format(num))

    even_count = 0
    odd_count = 0

    while num:
        if num < 0:
            num = -num
        if num % 10 == 0:
            even_count += 1
        else:
            odd_count += 1
        num /= 10
    return (even_count, odd_count)

