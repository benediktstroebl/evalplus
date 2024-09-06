
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    if num < 0:
        num *= -1
    num_len = len(str(num))
    for i in range(0, num_len):
        last_digit = int(str(num)[i])
        if last_digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

