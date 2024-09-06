
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = -num

    num_even = 0
    num_odd = 0

    while num > 0:
        digit = num % 10
        num //= 10
        if digit % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

    return num_even, num_odd


