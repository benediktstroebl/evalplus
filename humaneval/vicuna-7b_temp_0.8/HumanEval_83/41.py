
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The number of n-digit numbers
    num = 1
    # The number of n-digit numbers starting with 1
    count = 0
    # The number of n-digit numbers ending with 1
    count1 = 0
    # Loop through the digits of n
    for i in range(n):
        # Loop through the digits of n
        for j in range(i+1, n):
            # If the current and next digits are 1, increment the count of
            # numbers ending with 1 and reset the count of numbers starting with 1
            if (j+1) % 10 == 1 and (i+1) % 10 == 1:
                count1 += 1
                count = 0
            # If the current digit is 1, increment the count of numbers starting with 1
            if i % 10 == 1:
                count += 1
    # Return the result
    return count + count1
