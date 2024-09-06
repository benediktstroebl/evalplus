
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    count = 0
    for i in range(10**(n-1), 10**n):
        digit_sum = sum([int(digit) for digit in str(i)])
        if digit_sum == n:
            count += 1
        elif digit_sum == n + 1:
            count += 1
    return count
