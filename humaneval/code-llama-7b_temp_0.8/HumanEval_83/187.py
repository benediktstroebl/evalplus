
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Get all n-digit numbers and count the number of numbers that start or end
    # with 1
    return len([number for number in range(1, 10**n) if (number//10**(n-1))%10 == 1 or number%10 == 1])
