def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Generate a list of integers from 0 to n-1.
    num_list = list(range(n))
    # Filter out numbers that are not divisible by 11 or 13.
    div_by_11_or_13 = [num for num in num_list if num % 11 == 0 or num % 13 == 0]
    # Count the number of 7's in the filtered list of integers.
    seven_count = sum(1 for num in div_by_11_or_13 if num % 10 == 7)
    return seven_count