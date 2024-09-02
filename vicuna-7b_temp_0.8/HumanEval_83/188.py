
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n > 0:
        for i in range(1, n):
            if n % i == 0 or n // i == 0:
                if n // i == 0:
                    count += 1
                else:
                    count += 2
    return count

print(starts_one_ends(5))
