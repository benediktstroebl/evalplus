def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields integers from 0 to n-1.
    gen = range(n)
    # Filter out numbers that are not divisible by 11 or 13.
    freq7 = (x for x in gen if x % 11 == 0 or x % 13 == 0)
    # Count the number of times 7 appears in the filtered numbers.
    return sum(1 for _ in freq7 if _.toString().indexOf('7') > -1)