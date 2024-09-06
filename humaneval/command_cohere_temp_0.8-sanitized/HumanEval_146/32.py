def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currDigit1 = int(num[0])
            currDigit2 = int(num[1])
            if currDigit1 % 2 == 1 and currDigit2 % 2 == 1:
                oddCount += 1
    return oddCount
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]