
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Use a hash to store the count of each n-digit positive integer
    # This way we can avoid computing the same count multiple times
    count = {str(i): 0 for i in range(10)}
    # Start counting the number of n-digit positive integers that start with 1
    count['1'] = 0
    # If n is 1, return 1
    if n == 1:
        return 1
    # Use a while loop to iterate through the digits of n
    # While the digit is greater than 0
    while True:
        # Get the digit of n
        digit = n % 10
        # If the digit is 1, increment the count of n-digit positive integers that start with 1
        if digit == 1:
            count['1'] += 1
        # If the digit is 0, increment the count of n-digit positive integers that end with 1
        elif digit == 0:
            count[str(n)] += 1
        # Otherwise, we have reached the end of the while loop
        else:
            break
    # If the digit is 0 and n is not 1, increment the count of n-digit positive integers that end with 0
    if digit == 0:
        for i in range(1, n+1):
            count[str(i)] += 1
    # Return the count of n-digit positive integers that start with 1 and/or end with 1
    return count['1'] + count[str(n)]