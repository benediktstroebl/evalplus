
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for number in range(1, n+1):
        number_str = str(number)
        if number_str[0] == '1':
            count += 1
