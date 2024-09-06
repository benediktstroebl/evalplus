def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            firstOdd = num % 2
            lastOdd = (num % 10) % 2
            if firstOdd and lastOdd:
                oddCounts += 1
    return oddCounts