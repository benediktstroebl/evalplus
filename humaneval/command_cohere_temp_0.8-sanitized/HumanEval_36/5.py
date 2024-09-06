def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers from 1 to n that are divisible by 11 or 13
    viable = [i for i in range(1, n+1) if i % 11 == 0 or i % 13 == 0]
    # Filter in the numbers with digit 7 from the above viable numbers
    sevens = [i for i in viable if 7 in str(i)]
    return len(sevens)