
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # your code here
    even = 0
    odd = 0
    negative = False
    if num < 0:
        negative = True
        num = num * -1
    while num > 0:
        temp = num % 10
        if temp % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd) if not negative else (-even, -odd)

