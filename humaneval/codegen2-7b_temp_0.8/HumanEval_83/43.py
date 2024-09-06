
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, 10 ** n):
        i_str = str(i)
        if i_str.startswith("1") or i_str.endswith("1"):
            count
