
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1,10):
        num = str(i)+str(n-1)+str(i)
        if num[0]=='1':
            count+=1
        if num[-1]=='1':
            count+=1
    return count
