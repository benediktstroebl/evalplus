def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count_ones function to count the number of digits in a number within a specific range of bases.
    def count_ones(num, base):
        return num // base + (num % base > 0)
    
    # Initialize the count of numbers that start or end with 1 to 0.
    count = 0
    # Iterate through bases from 1 to n * 2.
    for base in range(1, n * 2 + 1):
        # Calculate the number of digits in the current base.
        num_digits = int(n * 2 ** (base - 1))
        # Calculate the count of ones at the end of the numbers in this base.
        ones_end = count_ones(num_digits, base)
        # Calculate the count of ones at the beginning of the numbers in this base.
        ones_start = count_ones(num_digits - 1, base)
        # Calculate the count of numbers that start or end with 1 in this base.
        count += ones_start + ones_end
    # Return the final count of numbers that start or end with 1.
    return count