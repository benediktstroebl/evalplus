
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num == 0:
        return (0, 0)
    
    odd_count, even_count = 0, 0
    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return (odd_count, even_count)
