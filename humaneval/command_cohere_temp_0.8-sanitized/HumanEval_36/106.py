def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers from 1 to n that are divisible by 11 or 13
    pertinent = [7] + [i for i in range(n+1) if i%11==0 or i%13==0]
    # Count the occurrences of digit 7 in the pertinent list
    return pertinent.count(7)