
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_digit_count = 0
    odd_digit_count = 0
    for x in str(num):
        if int(x) % 2 == 0:
            even_digit_count += 1
        else:
            odd_digit_count += 1

    return even_digit_count, odd_digit_
