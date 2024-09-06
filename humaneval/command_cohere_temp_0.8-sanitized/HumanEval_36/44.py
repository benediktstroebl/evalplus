def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers from 1 to n that are divisible by 11 or 13.
    dr1, dr2 = divmod(n, 11), divmod(n, 13)
    divisors = [i for i in range(1, n + 1, 2 if dr1[1] or dr2[1] else 1)]
    # Filter out the numbers in the above list that have a digit 7.
    numbers_with_7 = [i for i in divisors if 7 in str(i)]
    return len(numbers_with_7)