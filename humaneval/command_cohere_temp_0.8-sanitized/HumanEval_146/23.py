def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigit1 = int(str(num)[0])
            currentDigit2 = int(str(num)[-1])
            if currentDigit1 % 2 == 1 and currentDigit2 % 2 == 1:
                oddCount += 1
    return oddCount