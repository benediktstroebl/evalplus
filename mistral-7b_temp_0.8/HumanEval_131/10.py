
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # 1. check whether n is even or odd, then check every odd digits of n
    # 2. return the product of those odd digits, or 0 if they're all even
    # 3. 0 < n <= 2147483647
    # 4. n is an integer
    # 5. odd numbers are always larger than 0
    # 6. the product of numbers won't exceed the limit of the int type
    # 7. No while loop, recursion or iteration
    if n % 2 == 0:
        return 0
    num = str(n)
    product = 1
    for i in range(len(num)):
        if int(num[i]) % 2 != 0:
            product *= int(num[i])
    return product
