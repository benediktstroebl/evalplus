def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields divisors of numbers less than n.
    divisors = (i for i in range(1, n + 1) if n % i == 0)
    # Filter out divisors that are divisible by 11 or 13.
    filtered = [i for i in divisors if i % 11 == 0 or i % 13 == 0]
    # Count the number of 7s in the filtered divisors.
    return sum(int(i) % 7 == 0 for i in filtered)