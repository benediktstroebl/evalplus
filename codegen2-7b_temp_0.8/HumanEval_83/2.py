
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for num in str(n):
        if num == "1":
            count += 1
        else:
            break
    return
