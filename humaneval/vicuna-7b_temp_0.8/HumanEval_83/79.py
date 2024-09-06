
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 if i % 2 == 0 or n % i == 0 else 0 for i in range(1, n+1))

@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 7, 8, 9])
