def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count list to store the counts of numbers starting or ending with 1 for each length
    count = [0] * (n + 1)
    # Initialize the count of n-digit numbers that start or end with 1 to 1
    count[n] = 1
    # Increase the count of n-digit numbers that start or end with 1 by 2 for each n-digit number that is less than 100
    for i in range(10, 100):
        count[n] += 2
        # Increase the count of (n-1)-digit numbers that start or end with 1 by 1 for each n-digit number that starts with 1
        if str(i).startswith('1'):
            count[n-1] += 1
        # Increase the count of (n-1)-digit numbers that start or end with 1 by 1 for each n-digit number that ends with 1
        if str(i).endswith('1'):
            count[n-1] += 1
    # Return the final count of n-digit positive integers that start or end with 1
    return count[n]