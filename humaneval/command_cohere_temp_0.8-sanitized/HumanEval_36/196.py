def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Generate a list of integers from 0 to n-1.
    less_than_n = list(range(n + 1))
    # Filter out numbers that are divisible by 11 or 13.
    divisors = [i for i in less_than_n if i % 11 == 0 or i % 13 == 0]
    # Count the number of 7s in the filtered list of divisors.
    return sum(1 for _ in range(len(divisors)) if divisors[_] == 7)