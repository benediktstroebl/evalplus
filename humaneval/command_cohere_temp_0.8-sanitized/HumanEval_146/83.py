def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            curr = str(num)
            if int(curr[0]) % 2 == 1 and int(curr[-1]) % 2 == 1:
                oddCount += 1
    return oddCount