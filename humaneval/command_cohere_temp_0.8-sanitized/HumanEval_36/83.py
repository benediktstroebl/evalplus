def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the numbers from 1 to n.
    numbers = list(range(1, n + 1))
    # Count the number of 7s in numbers divisible by 11 or 13.
    return sum(1 for number in numbers if divmod(number, 11) == (1, 0) or divmod(number, 13) == (1, 0) and 7 in str(number))