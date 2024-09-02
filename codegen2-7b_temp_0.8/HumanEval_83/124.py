
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    while True:
        if n % 10 == 1 or n % 10 == 9:
            count += 1
        if n % 10 == 0:
            break
        n //= 10
    
