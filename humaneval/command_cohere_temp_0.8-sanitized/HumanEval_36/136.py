def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields integers from 0 to n-1 that are divisible by 11 or 13.
    relevant_integers = (x for x in range(n) if x % 11 == 0 or x % 13 == 0)
    # Filter the generator expression to retain only integers containing 7.
    sevens = [x for x in relevant_integers if 7 in str(x)]
    # Count and return the number of integers containing 7.
    return len(sevens)