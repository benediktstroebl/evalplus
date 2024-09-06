
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 10 is the maximum number of digits of the input n
    # we need to use a while loop for this problem, as we need to check
    # all possible combinations of the digits, in this case 10^3 = 1000
    # iterations
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 10:
        return 0
    elif n in (10, 11):
        return 1
    else:
        n = str(n)
        count = 0
        for i in range(1000):
            for j in range(n-1, 1, -1):
                if j == 1 or n % j == 0:
                    if n % j == 1:
                        count += 1
        return count
