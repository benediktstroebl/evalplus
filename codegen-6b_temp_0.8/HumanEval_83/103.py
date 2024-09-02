
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    n_factorial = math.factorial(n)
    memo = {}
    for i in range(1, n+1):
        for j in range(math.floor(n_factorial/i), math.ceil(n_factorial/i) + 1):
            t = i * j
            if t in memo:
                count += memo[t]
            else:
                memo[t] = 1
    return count

