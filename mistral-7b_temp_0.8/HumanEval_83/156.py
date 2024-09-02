
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    x=1
    ans=0
    while x<10**(n-1):
        if x%10==1:
            if (x+1)%10==1:
                ans+=1
        x+=1
    return ans
