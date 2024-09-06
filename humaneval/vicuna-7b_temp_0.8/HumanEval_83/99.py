
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Note: This is a brute-force solution, but it's the simplest one.
    # There might be a more efficient way to solve this problem, but it
    # would require more advanced techniques and would be less clear.
    return (2 + sum(1 for i in range(n) if i % 2 == 0))
