
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Handle the base case when n < 10
    if n < 10:
        return 1
    
    # Handle the case when n is 1
    if n == 1:
        return 1
    
    # Handle the case when n is 2
    if n == 2:
        return 2
    
    # The number of digits in n-1
    digits = (n-1)
    
    # Count the number of 1s in n-1 and n-2, respectively
    count_n_1s = 0
    count_n_2s = 0
    
    for i in range(digits-1, -1, -1):
        if n % i == 0:
            count_n_1s += 1
        else:
            count_n_2s += 1
    
    # Return the sum of the count of 1s in n-1 and n-2
    return count_n_1s + count_n_2s
