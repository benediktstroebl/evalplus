def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigitSum = sum(map(int, str(num)))
            if currentDigitSum % 2 == 1 and currentDigitSum == num % 100:
                oddCount += 1
    return oddCount