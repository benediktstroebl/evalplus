
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0

    for i in range(1, 10 ** n):
        digit_sum = 0
        for j in str(i):
            digit_sum += int(j)
        if digit_sum == 1 or (digit_sum > 9 and digit_sum % 10 == 1):
            count += 1

    return count

