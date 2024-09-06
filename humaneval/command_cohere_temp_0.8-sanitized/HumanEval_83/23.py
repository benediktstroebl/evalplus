def starts_one_ends(n):
    # Create a list to store the results for base cases and corners.
    # Also, since the answer should be integer, we'll use `int` type.
    return int(n <= 2 or n >= 10) + sum(int(d == 1 or d == n) for d in range(2, n))