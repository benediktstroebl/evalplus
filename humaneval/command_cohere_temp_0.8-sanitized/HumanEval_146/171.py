def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            curr = int(str(num)[0])
            last = int(str(num)[-1])
            if curr % 2 == 1 and last % 2 == 1:
                oddCount += 1
    return oddCount