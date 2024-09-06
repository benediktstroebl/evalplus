
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    even_digit = 0
    odd_digit = 0

    if num < 0:
        num = abs(num)
        even_digit = 1
    
    while num > 0:
        remainder = num % 10
        if remainder % 2 == 0:
            even_digit += 1
        else:
            odd_digit += 1
        num = num // 10

    return (even_digit, odd_digit)
