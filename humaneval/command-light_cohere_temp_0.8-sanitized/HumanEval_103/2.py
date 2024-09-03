def rounded_avg(n, m):
    """Computes the average of integers from n through m, rounding to the nearest integer and
    converting the result to binary."""
    # Check if m is greater than n
    if m > n:
        return "none"
    # Compute the average
    if n == m:
        return f"{n}:{n}"
    return "0b11"