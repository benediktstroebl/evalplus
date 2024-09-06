def specialFilter(nums):
    oddFirst = [x for x in nums if int(x[0]) % 2 == 1 and int(x[1]) % 2 == 1 and x > 10]
    return len(oddFirst)