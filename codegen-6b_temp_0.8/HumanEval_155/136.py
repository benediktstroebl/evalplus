
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    if num < 0:
        num = abs(num)
        below_zero = True
    else:
        below_zero = False
    while num > 0:
        digit = num % 10
        if below_zero:
            digit = abs(digit)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num /= 10
    return (even, odd)


