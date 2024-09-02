
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    if n == 2:
        return 10
    
    curr = 0
    count = 0
    for i in range(1, 10):
        curr = i * (n - 1)
        if curr % 10 == 1:
            count += 9 * (10 ** (n - 2))
        else:
            count += 9 * (10 ** (n - 2)) - (curr % 10 - 1)
        
        for j in range(1, 10):
            curr = i * (n - 1) + j * (n - 2)
            if curr % 10 == 1:
                count += 9 * (10 ** (n - 3))
            else:
                count += 9 * (10 ** (n - 3)) - (curr % 10 - 1)
            
            for k in range(1, 10):
                curr = i * (n - 1) + j * (n - 2) + k * (n - 3)
                if curr % 10 == 1:
                    count += 9 * (10 ** (n - 4
