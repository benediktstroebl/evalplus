
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    e_count = 0
    o_count = 0

    while num != 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            e_count += 1
        else:
            o_count += 1
        num //= 10
    return (e_count, o_count)
