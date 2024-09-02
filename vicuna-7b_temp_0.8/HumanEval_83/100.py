
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def f(n):
        # Base case
        if n <= 1:
            return 1
        # Recursive case
        return f(n-1) + f(n//10) + f(n//100)
    return f(n)
