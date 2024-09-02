
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (1, 0)

    if num < 0:
        num = -num

    even = 1 if num % 2 == 0 else 0

    while num > 0:
        num //= 10
        even += 1

    return (even - 1, even - 1) if even % 2 == 0 else (even - 1, even)

