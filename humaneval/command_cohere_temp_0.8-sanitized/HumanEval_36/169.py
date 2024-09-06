def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of the divisible numbers less than n.
    numbers = [i for i in range(1, n+1)]
    # Filter the list to only numbers that are divisible by 11 or 13.
    numbers = [i for i in numbers if i % 11 == 0 or i % 13 == 0]
    # Count the number of times the digit 7 appears.
    sevens = sum(1 for num in numbers if num % 10 == 7)
    return sevens