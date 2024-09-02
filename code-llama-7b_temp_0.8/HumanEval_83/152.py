
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    first = second = third = fourth = 0
    if n == 1:
        first = 1
    elif n == 2:
        first = 1
        second = 1
    elif n == 3:
        first = 1
        second = 1
        third = 1
    else:
        first = 1
        second = 1
        third = 1
        fourth = 1

    for i in range(10**(n-1), 10**n):
        num = str(i)
        if num[0] == '1' or num[-1] == '1':
            first += 1
        if num[0] == '1' and num[1] == '0' or num[-1] == '0' and num[-2] == '1':
            second += 1
        if num[0] == '1' and num[1] == '0' and num[2] == '0' or num[-1] == '0' and num[-2] == '0' and num[-3] == '1':
            third += 1
        if num[0] == '1' and num[1] == '0' and num[2] == '0' and num[3] == '0' or num[-1] == '0' and num[-2] == '0' and num[-3] == '0' and num[-4] == '1':
            fourth += 1
    return first + second + third + fourth
