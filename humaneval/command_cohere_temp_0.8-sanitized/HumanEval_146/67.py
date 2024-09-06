def specialFilter(nums):
    oddFirst = [x for x in nums if int(x[0]) % 2 == 1]
    oddLast = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirst & oddLast)