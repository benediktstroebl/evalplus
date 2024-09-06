
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num < 0:
        num = abs(num)

    num_digits = len(str(num))
    num_even = num_digits
    num_odd = 0

    while num_even >= 1:
        num_even -= 1
        num_odd += 1
        if num % 10 == 0:
            num_odd -= 1
        num //= 10
    return num_even, num_odd
