
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The integer n must be positive, otherwise we will raise a ValueError
    if n <= 0:
        raise ValueError("n must be positive!")
    
    # Initialize the counter of integers starting or ending with 1
    starts = 0
    
    # The last digit of the number must be 1, otherwise we return 0
    # There are n digits in the number, so the total number of 
    # such numbers is n! / (n-1)!
    # Start with 1, 2, ... 10, and then we subtract 9 from 10.
    # And then 9 from 10, ... 2, and then 1 from 2.
    # So we count 9! + 8! + ... + 2! + 1! = 9*10*11*...*n / (n-1) =
    # n * (n+1) * ... * (n+n-1) = n * (n+n-1) / 2 = n * n / 2 = n^2 / 2
    for i in range(1, n+1):
        starts += n*i // 2
    return starts
