def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            currOddCounts = 0
            currOddCounts += 1 if num % 3 == 1 else 0  
            currOddCounts += 1 if num // 10 % 3 == 1 else 0  
            if currOddCounts > 0:
                oddCounts += 1
    return oddCounts