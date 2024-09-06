
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(int(digit) == 1 or (int(digit) == 2 and int(str(int(digit))[0])!= 0) for digit in str(n
