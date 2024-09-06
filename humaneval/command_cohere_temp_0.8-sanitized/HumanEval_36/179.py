def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, include only those divisible by 11 or 13
    candidates = [num for num in range(n + 1)] if n > 1 else [0]
    filter_func = lambda x: (x % 11 == 0 or x % 13 == 0) and x <= n
    filtered_numbers = list(filter(filter_func, candidates))
    
    # Count occurrences of digit 7 in filtered numbers
    sevens = sum(1 for num in filtered_numbers if num % 10 == 7)
    return sevens