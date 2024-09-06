
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 10 is the smallest number that ends with 1
    count = 10
    if n % 10 == 0:
        count += n // 10
    return count
