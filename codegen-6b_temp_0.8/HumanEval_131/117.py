
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    while n > 0:
        if n % 2 == 1:
            return (n * (n // 10))
        n = n // 10
    return 0

    # for _ in range(1, n):
    #     if n % 2 == 1:
    #         return n
    #     n = n // 10
    # return 0

