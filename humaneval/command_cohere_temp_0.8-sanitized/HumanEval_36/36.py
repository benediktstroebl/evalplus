def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the results of dividing numbers by 13:
    thirteen_results = [i for i in range(1, n+1, 13)]
    # Define a list to store the results of dividing numbers by 11:
    eleven_results = [i for i in range(1, n+1, 11)]
    # Combine the results from the two lists:
    return sum(seven_cnt for thirteen_group in thirteen_results for seven_cnt in [eleven_results.count(eleven_group) for eleven_group in thirteen_group if int(eleven_group) % 7 == 7])