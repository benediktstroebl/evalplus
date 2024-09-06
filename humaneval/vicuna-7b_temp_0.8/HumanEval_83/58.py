
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n should be at least 2, otherwise return 0
    if n < 2:
        return 0
    # store the digits as an array
    digits = str(n).split(' ')
    # count the number of 1-starting numbers
    count1 = 0
    for digit in digits:
        if digit == '1':
            count1 += 1
    # count the number of 1-ending numbers
    count2 = 0
    for digit in reversed(digits):
        if digit == '1':
            count2 += 1
    # return the sum of the counts
    return count1 + count2
