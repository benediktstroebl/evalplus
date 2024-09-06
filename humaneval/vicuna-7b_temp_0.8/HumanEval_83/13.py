
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # ...
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    # 1 1 1 1 1 1 1 1 1 1
    if n == 1:
        return 0
    # Check the rightmost digit
    if n % 10 == 1:
        return (n // 10) + (1 if n % 100 == 1 else 0)
    # Check the leftmost digit
    if n % 10 == 1:
        return (n // 10) + (1 if n % 100 == 1 else 0)
    # Check the middle digits
    middle = n // 10
    middle_1s = 0
    middle_0s = 0
    for i in range(1, middle + 1):
        if n % 10 == i:
            middle_1s += 1
        else:
            middle_0s += 1
    return middle + middle_1s
