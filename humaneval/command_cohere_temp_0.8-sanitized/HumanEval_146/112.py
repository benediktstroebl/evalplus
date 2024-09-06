def specialFilter(nums):
    odd_digits = [int(num) for num in nums if num > 10 and (num % 10 != 0 or num // 10 != 0)]
    return len(odd_digits)