def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the numbers from 1 to n.
    numbers = list(range(1, n + 1))
    # Count the number of times 7 appears in numbers divisible by 11 or 13.
    return sum(1 for num in numbers if num % 11 == 0 or num % 13 == 0 and '7' in str(num))