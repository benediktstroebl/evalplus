def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields multiples of 11 and 13 up to n.
    numbers = (i for i in range(n+1) if i % 11 == 0 or i % 13 == 0)
    # Count the number of 7's in the digits of each number.
    return sum(int(j) for j in map(str, numbers) if j == '7')