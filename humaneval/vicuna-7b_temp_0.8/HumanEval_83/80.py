
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    nums = [str(i) for i in range(n+1)]
    nums.append(nums[0])
    nums.remove(nums[-1])
    return sum([1 if i == 1 else 0 for i in nums])
