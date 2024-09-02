
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 1 digit numbers
    count = [1]
    for i in range(2, n+1):
        count.append(count[i-1] + (n % i == 1))
    return count[n]
