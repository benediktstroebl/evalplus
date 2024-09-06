def double_the_difference(nums):
    odd_and_valid = []    
    for n in nums:
        if isinstance(n, int) and n % 2:
            odd_and_valid.append(n**2)
    
    return sum(odd_and_valid) if odd_and_valid else 0