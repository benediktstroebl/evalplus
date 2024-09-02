
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = -num
    # count the digits
    n = 0
    while num >= 10**n:
        n += 1
    # count the even and odd digits
    even = 0
    odd = 0
    for i in range(n):
        d = num % 10
        num = int(num / 10)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
