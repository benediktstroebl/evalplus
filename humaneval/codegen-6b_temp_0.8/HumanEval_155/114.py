
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError('Number should be a positive value')
    even, odd = 0, 0
    while num:
        half = num // 10
        remainder = num % 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        num = half
    return even, odd

