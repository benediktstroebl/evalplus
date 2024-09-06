def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigits = [int(digit) for digit in str(num)]
            if currentDigits[0] % 2 == 1 and currentDigits[-1] % 2 == 1:
                oddCount += 1
    return oddCount
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]