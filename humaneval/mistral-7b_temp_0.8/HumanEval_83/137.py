
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    result = 0
    for i in range(1,n+1):
        # all possibilities for the first and last digits
        first_digit = 1
        last_digit = 1
        num = str(first_digit)
        num += str(last_digit)
        for i in range(n-2):
            # numbers in between must be positive
            num += str(i+2)

        result += 1
    return result
