def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of the divisible numbers less than n.
    nums = [i for i in range(1, n+1)]
    # Filter out the numbers that are divisible by 11 or 13.
    divisible = [i for i in nums if i % 11 == 0 or i % 13 == 0]
    # Count the number of times 7 appears in the filtered list.
    return sum(1 for _ in divisible if _.toString().indexOf('7') > -1)