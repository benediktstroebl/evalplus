
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num < 0:
        return(0, 1)
    else:
        count = 0
        while num:
            num, rem = divmod(num, 10)
            count += 1 if rem % 2 else 0
        return(count, count - 1)

