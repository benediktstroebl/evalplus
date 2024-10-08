
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise ValueError("The input must be an integer")

    if num == 0:
        return (1, 0)
    if num < 0:
        num *= -1

    even = 0
    odd = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd)

