
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    odd = 0
    even = 0
    while num!= 0:
        odd += 1
        num = num // 10
    while odd % 2 == 0:
        even += 1
        odd //= 2
    return (even, odd)


