def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields integers from 0 to n-1 that are divisible by 11 or 13.
    numbered = (i for i in range(n) if i % 11 == 0 or i % 13 == 0)
    # Filter the generator expression to only include integers that have a digit 7.
    sevens = (i for i in numbered if 7 in str(i))
    # Count the number of integers in the filtered list and return the count.
    return sum(map(lambda x: 1, sevens))