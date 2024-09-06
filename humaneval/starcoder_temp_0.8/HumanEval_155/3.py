
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # your code here
    even, odd = 0, 0
    if num < 0:
        num *= -1
    while num:
        last_digit = num % 10
        num //= 10
        if last_digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
