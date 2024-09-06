
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here

    # Solution 1: Using str()
    # if n == 0: return 0
    # s = str(n)
    # res = 1
    # for ch in s:
    #     if int(ch) % 2 != 0:
    #         res *= int(ch)
    # return res

    # Solution 2: Using digit() and divide 10
    if n == 0: return 0
    res = 1
    while n != 0:
        last_digit = n % 10
        if last_digit % 2 != 0:
            res *= last_digit
        n //= 10
    return res

    # Solution 3: Using % and divide 10
    if n == 0: return 0
    res = 1
    while n % 2 == 0:
        n //= 2
    while n != 0:
        last_digit = n % 10
        if last_digit % 2 != 0:
            res *= last_digit
        n //= 10
    return res

    # Solution 4: Using % and divide 10, with pair-wise swap
    if n == 0: return 0
    res = 1
    while n % 2 == 0:
        n //= 2
    while n != 0:
        if n % 2 != 0:
            res *= n % 10
        n = n // 10
    return res


    # Solution 5: Using % and divide 10, with swapping
    if n == 0: return 0
    res = 1
    while n % 2 == 0:
        n //= 2
    while n != 0:
        if n % 2 != 0:
            temp = n % 10
            n //= 10
            n += temp
            res *= temp
        n //= 10
    return res

    # Solution 6: Using % and divide 10, with swapping, and final swap
    if n == 
