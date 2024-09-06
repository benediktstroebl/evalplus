
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    digits = str(abs(num))
    n = len(digits)
    even_count = 0
    odd_count = 0
    for i in range(n):
        if digits[i] == '0':
            even_count += 1
        else:
            odd_count += 1
    return n, even_count, odd_count
