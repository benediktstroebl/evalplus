def specialFilter(nums):
    odd_digits = [int(i) for i in nums if i % 2 != 0 and int(i) % 10 != 0]
    return len(odd_digits)