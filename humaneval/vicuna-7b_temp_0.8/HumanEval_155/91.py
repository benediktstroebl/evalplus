
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # return a tuple of the number of even and odd digits in a number
    n = len(str(num))
    evens = 0
    odds = 0
    for i in range(n):
        if num > 0:
            evens += num % 2 == 0
        num //= 10
    for i in range(n):
        if num > 0:
            odds += num % 2 == 1
        num //= 10
    return (evens, odds)