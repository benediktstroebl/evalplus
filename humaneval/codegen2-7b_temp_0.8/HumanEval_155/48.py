
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError
    odd, even = 0, 0
    while num!= 0:
        if num % 10 == 0:
            odd += 1
        else:
            even += 1
        num //= 10
    return odd, even

