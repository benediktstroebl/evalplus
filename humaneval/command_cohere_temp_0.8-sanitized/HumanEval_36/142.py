def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, include only those divisible by 11 or 13
    relevant_numbers = [num for num in range(n) if num % 11 == 0 or num % 13 == 0]
    # Count the number of 7s in the filtered numbers
    seven_count = sum(1 for num in relevant_numbers if num % 7 == 0)
    return seven_count