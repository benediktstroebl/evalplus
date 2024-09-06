
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # create a list of n-digit positive integers
    nums = [str(i) for i in range(10**n)]
    
    # for each number, check if it starts or ends with 1
    count = 0
    for num in nums:
        if (num[0] == '1' or num[-1] == '1') and len(num) == n:
            count += 1
            
    return count
