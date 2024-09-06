
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    number = num
    count = 0
    if number < 0:
        number *= -1
    while number > 0:
        if number % 10 == 0:
            count += 1
        number //= 10
    even = 0
    odd = 0
    number = num
    if number < 0:
        number *= -1
    while number > 0:
        if number % 10 == 0:
            even += 1
        elif number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10
    if num < 0:
        if even == 0:
            even += 1
        if odd == 0:
            odd += 1
    return (even, odd)
