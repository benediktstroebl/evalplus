def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Generate a list of integers from 0 to n-1.
    integers = list(range(n))
    # Filter out numbers that are not divisible by 11 or 13.
    divisors = [i for i in integers if i % 11 == 0 or i % 13 == 0]
    # Count the number of times 7 appears in the filtered list of divisors.
    return divisors.count(7)