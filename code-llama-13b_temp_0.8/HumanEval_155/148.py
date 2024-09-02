
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = -num
    result_odd = result_even = 0
    while num > 0:
        if num % 10 % 2 == 0:
            result_even += 1
        else:
            result_odd += 1
        num //= 10
    return (result_even, result_odd)

