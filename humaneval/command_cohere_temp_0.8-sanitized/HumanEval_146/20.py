def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currDigitSum = sum(map(int, str(num)))
            if currDigitSum % 2 == 1 and currDigitSum != 0:
                oddCount += 1
    return oddCount