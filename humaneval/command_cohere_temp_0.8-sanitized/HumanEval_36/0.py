import math
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Calculate the ceiling value of n/11 and n/13
    m11, m13 = (n + 10) // 11, (n + 12) // 13
    # Calculate the expected count of 7s
    count = (m11 + m13) * 2
    # Adjust the count for n being a multiple of both 11 and 13
    if n == 11 * 13:
        count -= 2
    return count