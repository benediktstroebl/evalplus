
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # print(n % 2)
    # if n % 2 == 0:
    #     return 0
    # else:
    #     return n % 10
    n = str(n)
    result = 1
    for i in range(len(n)):
        # print(n[i], end=' ')
        if int(n[i]) % 2 == 1:
            result = result * int(n[i])
        # print('result =', result)
    return result

