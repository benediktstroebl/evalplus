def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the numbers from 1 to n.
    numbers = list(range(1, n + 1))
    # Count the number of times 7 appears in numbers divisible by 11 or 13.
    count = sum(1 for number in numbers if int(str(number)[:1]) == 7 and (number % 11 == 0 or number % 13 == 0))
    return count