
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    digits = str(abs(num))
    if digits[0] == '0':
        digits = digits[1:]
    n = 0
    for i in range(len(digits)):
        if digits[i] == '0':
            n += 1
        else:
            n += 1 if (i + 1) % 2 == 0 else 1
    return n // 2, n % 2
