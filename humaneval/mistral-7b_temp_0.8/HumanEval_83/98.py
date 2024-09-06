
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    # Start with an empty list
    count = []

    # Loop from 1 to n
    for num in range(1, n+1):

        # For every number in the range
        if str(num)[0] == "1":
            count.append(num)

        if str(num)[-1] == "1":
            count.append(num)

    # Return the count
    return len(count)
