
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n-1 digit numbers
    num1 = 1
    num2 = 2
    num3 = 3
    count1 = 0
    count2 = 0

    for i in range(n):
        count1 += (n//i == 1)
        count2 += (n//i == n-i)
    return count1 + count2
