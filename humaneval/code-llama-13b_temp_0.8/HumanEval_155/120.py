
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise TypeError('The number must be an integer')

    even = 0
    odd = 0
    while num > 0:
        if num % 10 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return even, odd
