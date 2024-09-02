
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    evens, odds = 0, 0
    while num:
        if num % 10 % 2:
            odds += 1
        else:
            evens += 1
        num //= 10
    return evens, odds


