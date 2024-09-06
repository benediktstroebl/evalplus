def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            currentDigitValue = int(str(num)[0])
            lastDigitValue = int(str(num)[-1])
            if currentDigitValue % 2 == 1 and lastDigitValue % 2 == 1:
                oddCounts += 1
    return oddCounts