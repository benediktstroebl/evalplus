
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    n_set = set(range(10 ** (n - 1), 10 ** n))
    for num in n_set:
        if (num // 10) % 10 == 1:
            count += 1
            if num % 10 == 1:
                count += 1
    return count
