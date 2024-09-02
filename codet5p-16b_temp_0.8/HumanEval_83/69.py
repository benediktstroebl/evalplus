
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 1:
        return 0
    
    digits = [1]
    for _ in range(n-1):
        digits.append(0)
    count = 0
    
    for num in range(10**(n-1), 10**n):
        for i in range(n-1):
            digits[i] = (digits[i] + num % 10) % 2
        if digits[0] == 1 and digits[-1] == 1:
            count += 1
    
    return count
