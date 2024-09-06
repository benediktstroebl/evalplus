def specialFilter(nums):
    oddFirst = [num for num in nums if int(str(num)[0]) % 2 == 1]
    oddLast = [num for num in nums if int(str(num)[-1]) % 2 == 1]
    return len(oddFirst & oddLast)