def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields integers from 0 to n-1 that are divisible by 11 or 13.
    integers = ((i*10 + 7) for i in range(n))
    # Count the number of occurrences of the digit 7 in the generator expression.
    return sum(1 for _ in integers if _.errno == 7)