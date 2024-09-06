
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def _ones(n):
        """
        Generate the numbers of n-digits that start with 1.
        """
        if n == 1:
            yield 1
        else:
            for i in range(1, 10):
                for rest in _ones(n - 1):
                    yield i * 10 + rest

    def _ends(n):
        """
        Generate the numbers of n-digits that end with 1.
        """
        if n == 1:
            yield 1
        else:
            for i in range(1, 10):
                for rest in _ones(n - 1):
                    yield rest + i * 10

    return sum(1 for i in _ones(n)) + sum(1 for i in _ends(n))

