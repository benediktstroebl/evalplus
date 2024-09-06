def specialFilter(nums):
    oddFirst = [num for num in nums if int(num[0]) % 2 == 1]
    oddLast = [num for num in oddFirst if int(num[-1]) % 2 == 1]
    return len(oddLast)