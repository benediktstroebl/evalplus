
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    if n == 2:
        return 1
    else:
        count = 0
        digit = n % 10
        for i in range(1, n):
            if (digit == 1 and (i % 2 == 0 or i % 3 == 0 or i % 4 == 0 or i % 5 == 0 or i % 6 == 0 or i % 7 == 0 or i % 8 == 0)) or \
               (digit != 1 and (i % 2 == 0 or i % 3 == 0 or i % 4 == 0 or i % 5 == 0 or i % 6 == 0 or i % 7 == 0 or i % 8 == 0)):
                count += 1
        return count
