
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 1-index
    count = 0
    # find the number of digits in n
    num_digits = len(str(n))
    # loop through n digits at a time
    for i in range(1, num_digits):
        # check if n starts with 1
        if n[i-1] == 1:
            count += 1
        # check if n ends with 1
        elif n[-i] == 1:
            count += 1
    return count