def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count list to store the counts of numbers starting or ending with 1.
    count = [0] * (n + 1)
    # Initialize the count of numbers starting or ending with 1 to the numbers from 1 to n.
    for num in range(1, n + 1):
        # For numbers with a length of 1 to n, increment the count if the number starts or ends with 1.
        if num % 10 == 1:
            count[num] += 1
    # Return the final count of numbers starting or ending with 1.
    return count[1] + count[n]