
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    num = 0
    for i in range(1, 10):
        num += int(str(1*10**(n-1) + i) + "1")
    for i in range(1, 10):
        num += int(str(1*10**(n-1)) + "1" + str(i*10))
    return num
