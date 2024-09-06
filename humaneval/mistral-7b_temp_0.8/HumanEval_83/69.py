
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    nums = []
    for i in range(1, 10):
        nums.append(i)
    for i in range(10):
        nums.append(10 * i + 1)
    for i in range(10, 100):
        nums.append(10 * i + 1)
    for i in range(100, 1000):
        nums.append(10 * i + 1)
    for i in range(1000, 10000):
        nums.append(10 * i + 1)
    for i in range(10000, 100000):
        nums.append(10 * i + 1)
    for i in range(100000, 1000000):
        nums.append(10 * i + 1)
    for i in range(1000000, 10000000):
        nums.append(10
