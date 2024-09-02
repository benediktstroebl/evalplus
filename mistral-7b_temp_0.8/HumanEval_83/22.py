
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num = 0
    n = int(n)
    while n != 0:
        n = int(n / 10)
        num += 1
    num = num**2
    for i in range(10**num, 10**(num+1)):
        if int(i / 100) == 1:
            num += 1
        elif int(i % 10) == 1:
            num += 1
    return num
