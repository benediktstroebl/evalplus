
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n % 10!= 1:
        return 0
    count = 0
    for i in range(1, n + 1):
        if str(i)[0] == "1":
            count += 1
    
