
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # get all n-digit numbers
    all_nums = list(range(10**(n-1), 10**n))
    # filter the numbers that start or end with 1
    nums = []
    for num in all_nums:
        if str(num)[:1] == '1' or str(num)[-1:] == '1':
            nums.append(num)
    return len(nums)
