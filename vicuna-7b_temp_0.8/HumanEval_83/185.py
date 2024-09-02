
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The two cases are similar, so it's easier to handle them together
    return (sum(1 for i in range(1, n+1) if str(i).startswith(str(n)[-1:])) +
            sum(1 for i in range(n+1, 10) if str(i).endswith(str(n)[-1:])) +
            sum(1 for i in range(1, n+1) if str(i).endswith(str(n)[-1:]) and
                 str(i)[-1] != str(n)[-1:]) +
            sum(1 for i in range(n+1, 10) if str(i).startswith(str(n)[-1:]) and
                 str(i)[-1] != str(n)[-1:])) -
            sum(1 for i in range(1, n+1) if str(i) in ['01', '10']))
