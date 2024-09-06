def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a list to store the digits of the number from the second to the last up to the last.
    num_digits = [0] * (n - 1) 
    # Define the list to store the count of numbers that start or end with 1.
    count = 0
    # Iterate through the numbers from 1 to n-1 that are less than n-digit positive numbers.
    for num in range(1, n - 1):
        # Append the current num to the num_digits list.
        num_digits[num - 1] = num
        # Increment the count if the number of digits is less than n.
        if len(str(num)) < n:
            count += 1
            # Decrement the count if the number of digits is exactly n.
        elif len(str(num)) == n:
            count -= 1
    return count