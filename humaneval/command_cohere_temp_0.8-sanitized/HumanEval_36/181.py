def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, include only those divisible by 11 or 13
    relevant_numbers = [i for i in range(n + 1) if i % 11 == 0 or i % 13 == 0]
    # Count the number of 7s in the filtered numbers
    return sum(1 for num in relevant_numbers if num % 7 == 0)