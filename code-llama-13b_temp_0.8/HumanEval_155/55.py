
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    n = abs(num)
    even = 0
    odd = 0
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    return even, odd
