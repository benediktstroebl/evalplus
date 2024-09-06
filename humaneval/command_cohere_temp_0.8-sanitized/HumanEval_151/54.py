def double_the_difference(nums):
    odd_sq = sum(n**2 for n in nums if n % 2 and n >= 0 and isinstance(n, int))
    return int(odd_sq)