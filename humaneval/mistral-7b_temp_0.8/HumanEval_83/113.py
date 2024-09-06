
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    # n  = input('Please enter a number')
    # n=int(n)
    if n==1:
        return 0
    elif n==2:
        return 0
    elif n==3:
        return 1
    else:
        x=n//10
        y=x%10
        if y==1:
            return 1+(n-1)
        else:
            x=n//100
            y=x%10
            if y==1:
                return 1+(n-1)
            else:
                z=n%10
                if z==1:
                    return 1+(n-1)
                else:
                    return 0



