
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, -1)
    if num == 0:
        return (0, 0)
    digits = str(num)
    odd_count = 0
    for i in range(len(digits) - 1):
        if digits[i] == '1' and digits[i + 1] == '1':
            odd_count += 1
        else:
            odd_count = 0
    even_count = digits.count('0')
    return (even_count, odd_count)
