
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num == 0:
        return 0, 0
    else:
        even = num % 2
        odd = abs(num % 2 - 1)
        return even_odd_count(num // 10) + (even, odd)
