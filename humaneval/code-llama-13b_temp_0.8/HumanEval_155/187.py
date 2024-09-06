
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num *= -1

    # if num is less than 10, it can't have more than 1 digit
    if num < 10:
        if num % 2 == 0:
            return (1, 0)
        else:
            return (0, 1)

    even = 0
    odd = 0
    while num > 0:
        if num % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        num /= 10

    return (even, odd)
