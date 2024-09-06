
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError("n must be >= 0")
    even = 0
    odd = 0
    while num:
        if num % 10 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd
