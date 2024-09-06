def fibfib(n):
    # Create an memoization dictionary with initial values:
    memo = {
        0: 0,
        1: 0,
        2: 1,
    }
    # Check if the result is already cached:
    if n in memo:
        return memo[n]
    # Otherwise, compute and store the result in the dictionary:
    if n >= 3:
        memo[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    # Return the final result:
    return memo[n]