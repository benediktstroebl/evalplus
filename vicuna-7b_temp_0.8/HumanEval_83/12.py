
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Handle base cases
    if n <= 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    
    # Generate all n-digit numbers and count the number that start or end with 1
    digits = [str(d) for d in range(1, 10)]
    result = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if str(i) + str(j) == str(n):
                result += 1
    
    # Return the result
    return result
