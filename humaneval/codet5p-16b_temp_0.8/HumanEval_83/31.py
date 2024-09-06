
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    nums = []
    for i in range(1, 10):
        for j in range(1, 10):
            nums.append(i*j)

    count = 0
    for num in nums:
        if num[0] == 1 or num[-1] == 1:
            count += 1
    return count
