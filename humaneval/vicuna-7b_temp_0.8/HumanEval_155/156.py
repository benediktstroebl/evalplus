
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    if digits[0] in ['-', '+']:
        digits = digits[1:]
    length = len(digits)
    count_even = 0
    count_odd = 0
    for i in range(length):
        if digits[i] in '01':
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
    return length, count_even, count_odd