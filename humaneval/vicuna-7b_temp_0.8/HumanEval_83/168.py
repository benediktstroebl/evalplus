
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n is odd, return 2
    if n % 2 == 1:
        return 2
    
    # count of numbers of n-digit positive integers that start with 1
    start_ones = 0
    for i in range(1, n+1):
        if i % 10 == 1:
            start_ones += 1
    
    # count of numbers of n-digit positive integers that end with 1
    end_ones = 0
    for i in range(1, n+1):
        if str(i)[-1] == '1':
            end_ones += 1
    
    # return the sum of the above two counts
    return start_ones + end_ones
