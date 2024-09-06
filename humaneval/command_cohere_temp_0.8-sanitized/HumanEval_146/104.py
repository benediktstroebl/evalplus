def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if currentDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCount += 1
    return oddCount
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]