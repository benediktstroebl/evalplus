
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Initialize the count and the current digit
    count = 0
    digit = 1
    # Keep looping until we get to the 10th digit
    while digit <= 9:
        # Set the counter to the correct value for this digit
        count += (n * digit)
        # Move on to the next digit
        digit += 1
    # Return the final count
    return count
