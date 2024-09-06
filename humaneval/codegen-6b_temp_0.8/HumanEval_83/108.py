
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 1
    
    memo = {}
    for i in range(10):
        memo[i] = int(math.pow(10, n-1))
    
    sum_i = 0
    for i in range(1, 10):
        sum_i += i
        memo[i] += sum_i
        
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                count += memo[i]
    return count
    
