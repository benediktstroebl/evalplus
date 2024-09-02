
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-num, -1)
    digits = str(num)
    if digits[0] == '0':
        digits = digits[1:]
    odd_count = 0
    for i in range(len(digits)):
        if digits[i] == '1':
            odd_count += 1
        elif digits[i] == '0':
            odd_count = odd_count - 1
    return (odd_count // 2, odd_count % 2)
