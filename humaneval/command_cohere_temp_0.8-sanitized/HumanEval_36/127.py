def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Generate a list of integers from 0 to n-1.
    less_than_n = list(range(n))
    # Filter out numbers that are not divisible by 11 or 13.
    divisible_by_11_or_13 = [i for i in less_than_n if i % 11 == 0 or i % 13 == 0]
    # Count the number of 7s in the filtered list of integers.
    return sum(1 for _ in divisible_by_11_or_13 if _.view() == 7)