
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError('Negative integers are not allowed')
    odd, even = num // 2, num // 2
    while even:
        odd, even = odd + even // 2, even // 2
    return (odd, even
