def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers from 1 to n that are divisible by 11 or 13
    relevant_numbers = [i for i in range(1, n+1) if i % 11 == 0 or i % 13 == 0]
    # Count the occurrences of digit 7 in the filtered numbers
    return sum(1 for num in relevant_numbers if '7' in str(num))