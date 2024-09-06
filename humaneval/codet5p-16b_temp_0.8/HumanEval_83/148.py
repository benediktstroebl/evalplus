
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 10

    l = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    for i in range(n - 1):
        l.append(0)
    
    for i in range(10):
        l[1] += i
        l[-1] += i
    
    for i in range(2, n):
        l[i] = l[i - 1] * i
    
    return sum(l)
