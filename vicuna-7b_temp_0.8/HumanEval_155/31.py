
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    sign = 0
    if num < 0:
        num = abs(num)
        sign = -1
    digits = []
    if num >= 0:
        i = 0
        while True:
            digit = num % 10
            if digit == 0:
                break
            digits.append(digit)
            num = num // 10
            i += 1
        num = num // 10
        while num > 0:
            digit = num % 10
            digits.append(digit)
            num = num // 10
    else:
        i = 1
        while num >= 10:
            digit = num % 10
            num = num // 10
            i += 1
            digits.append(digit)
    return (len(digits) // 2, (len(digits) % 2) + 1)
