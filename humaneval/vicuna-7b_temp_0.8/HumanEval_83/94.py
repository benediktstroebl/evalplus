
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case: If n is 1, return 2.
    if n == 1:
        return 2

    # Loop through the digits of n and count the number of 1-digits
    # that start or end with 1.
    count = 0
    for i in range(len(str(n))):
        if n[i] == '1':
            count += 1

    # Loop through the digits of n again and count the number of 1-digits
    # that start with 1 but end with 0.
    for i in range(len(str(n))):
        if n[i] == '1' and n[i+1:].isdigit() and int(n[i+1:]) != i+1:
            count += 1

    # Return the count
    return count
