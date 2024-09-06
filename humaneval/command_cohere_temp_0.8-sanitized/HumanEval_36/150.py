def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, including n itself.
    numbers = list(range(n + 1))
    # Generate all possible values less than or equal to n.
    multiples_of_11 = [i for i in numbers if i % 11 == 0]
    multiples_of_13 = [i for i in numbers if i % 13 == 0]
    # Intersect multiples of both 11 and 13 to get the list of interest.
    relevant_numbers = [i for i in multiples_of_11 if i in multiples_of_13]
    return sum(1 for num in relevant_numbers if '7' in str(num))