
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if not n:
        return 0
    if n == 1:
        return 10
    nums = set()
    # generate all possible starting numbers
    for i in range(10):
        nums.add(10**(n-2) * i + 1)
        nums.add(10**(n-1) + i)
    return len(nums)

