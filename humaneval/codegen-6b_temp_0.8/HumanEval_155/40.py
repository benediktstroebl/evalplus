
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    v = abs(num)
    even = 0
    odd = 0

    while v > 0:
        digit = v % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        v = v // 10

    return (even, odd)

