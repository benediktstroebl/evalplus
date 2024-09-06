
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Check that n is greater than 0
    if n > 0:
        # Check that n is a positive integer
        if n == int(n):
            # Initialize a variable to store the count of numbers that start with 1
            ones_start = 0
            # Initialize a variable to store the count of numbers that end with 1
            ones_end = 0
            # Iterate over the digits of n
            for i in range(1, n + 1):
                # Multiply the current digit by 10 to get the next digit in the number
                x = 10 ** (i - 1)
                # Increment the count of numbers that start with 1
                ones_start += x
                # Increment the count of numbers that end with 1
                ones_end += x
            # Return the sum of the counts
            return ones_start + ones_end
        else:
            # Return None if n is not a positive integer
            return None
    else:
        # Return None if n is not greater than 0
        return None
