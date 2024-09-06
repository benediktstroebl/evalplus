def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields divisors of numbers less than n.
    divisors = (i for i in range(1, n + 1) if n % i == 0)
    # Filter out divisors that are divisible by 11 or 13.
    filtered_divisors = filter(lambda x: x % 24 == 0, divisors)
    # Count the number of occurrences of digit 7 in the filtered divisors.
    return sum(int(d) for d in filtered_divisors if d % 10 == 7)