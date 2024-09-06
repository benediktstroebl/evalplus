
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    if num < 0:
        num = abs(num)
        negativeFlag = True
    else:
        negativeFlag = False
    while num:
        if num & 1:
            odd += 1
        else:
            even += 1
        num >>= 1
    if negativeFlag:
        return -1*even, -1*odd
    else:
        return even, odd

