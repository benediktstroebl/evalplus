def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of diving each integer from 1 to n against 13.
    num = [i for i in range(1, n+1)]
    # Apply the filter function to remove integers that are not divisible by 13.
    num = filter(lambda x: x % 13 == 0, num)
    # Count the number of integers in the list to get the number of times the digit 7 appears in integers less than n which are divisible by 13.
    seven_count = sum(num)
    # Define a list to store the results of diving each integer from 1 to n against 11.
    num = [i for i in range(1, n+1)]
    # Apply the filter function to remove integers that are not divisible by 11.
    num = filter(lambda x: x % 11 == 0, num)
    # Count the number of integers in the list to get the number of times the digit 7 appears in integers less than n which are divisible by 11.
    seven_count += sum(num)
    return seven_count