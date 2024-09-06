import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution, if multiple solutions exist.
    Only accepts lists of coefficients with an even number of items
    and the largest non-zero coefficient first, which guarantees
    a solution.
    """
    # your code here, try debugging with print statements
    # Bruteforce: Divide range intimately by 2 til find solution
    # Or Kendrick's algorithm 
    lst = [0] + coefficients[:0:-1]
    fac = [math.factorial for _ in range(len(lst) + 1)]
    ans = 0
    for i in range(len(lst)):
        temp = lst[i]
        for j in range(len(fac)):
            n = i + j + 1
            k = n // 2 + 1
            ans += temp / fac[n] * math.pow(2, k - 1) * math.factorial(k) / fac[k]
    return ans