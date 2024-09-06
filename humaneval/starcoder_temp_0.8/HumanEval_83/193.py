
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0
    for i in range(1, n + 1):
        num = i
        while num:
            if num % 10 == 1:
                total += 1
            num //= 10
        num = i
        while num % 10 == 1:
            num //= 10
            total += 1
    return total
