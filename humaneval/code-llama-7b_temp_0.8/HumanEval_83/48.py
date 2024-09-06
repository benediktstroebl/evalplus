
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # nums = [10**(i-1) + 1 for i in range(1, n+1)]
    # print(nums)
    # print(len(nums))
    # for i in nums:
    #     print(i)
    #     print(i % 10)
    #     print(i // 10)
    #     if i // 10 == 1 or i % 10 == 1:
    #         print(i)
    #         count += 1
    # return count
    count = 0
    for i in range(1, n+1):
        if i//10 == 1 or i % 10 == 1:
            count += 2
    return count
