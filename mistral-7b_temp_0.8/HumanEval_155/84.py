
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_num, odd_num = 0, 0
    while num > 0:
        last_num = num % 10
        if last_num % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
        num //= 10
    return even_num, odd_num

