def specialFilter(nums):
    oddDigits = [x for x in nums if int(x[0]) % 2 != int(x[1]) % 2]
    return len(oddDigits)