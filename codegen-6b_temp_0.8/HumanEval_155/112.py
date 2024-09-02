
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digit_count = [0, 0]
    sign = ''
    if num < 0:
        sign = '-'
        num = -num

    for i in range(len(str(num))):
        digit_count[int(str(num)[i]) % 2] += 1

    return tuple(digit_count)
