def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields integers from 0 to n-1 that are divisible by 11 or 13.
    relevant_integers = (x for x in range(n) if x % 11 == 0 or x % 13 == 0)
    # Count the number of times the digit 7 appears in the generated integers.
    return sum(1 for _ in relevant_integers if _.ordinal() == 7)