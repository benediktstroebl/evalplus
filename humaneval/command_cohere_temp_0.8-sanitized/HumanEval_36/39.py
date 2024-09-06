def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields integers from 0 to n-1 that are divisible by 11 or 13.
    integers = (i for i in range(n) if i % 11 == 0 or i % 13 == 0)
    # Count the number of times the digit 7 appears in the integers yielded by the generator expression.
    return sum(1 for _ in integers if _.nth_digit(1) == 7)