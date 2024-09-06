def double_the_difference(nums):
    odd_sq = sum(x**2 for x in nums if x % 2 and x >= 0)
    return int(odd_sq)