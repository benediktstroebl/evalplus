def double_the_difference(nums):
    odd_and_valid = []   
    for num in nums:
        if isinstance(num, int) and num % 2:
            odd_and_valid.append(num)
    return sum(x * x for x in odd_and_valid)