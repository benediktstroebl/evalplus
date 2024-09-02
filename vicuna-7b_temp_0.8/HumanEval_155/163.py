
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-num, 0)
    if num == 0:
        return (0, 1)
    digits = str(num)
    if digits[0] == '0':
        digits = digits[1:]
    if digits[0] % 2 == 0:
        count = 0
        for i in range(1, len(digits)):
            if digits[i] % 2 == 0:
                count += 1
        return (count, count)
    else:
        count = 1
        for i in range(1, len(digits)):
            if digits[i] % 2 != 0:
                count += 1
        return (count, count+1)
