def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers with 7 and divisible by 11 or 13 from the range below n
    relevant_numbers = [7*i//11 for i in range(1, n+1, 11)] + [7*i//13 for i in range(1, n+1, 13)]
    return sum(filter(lambda x: x == 7, relevant_numbers))