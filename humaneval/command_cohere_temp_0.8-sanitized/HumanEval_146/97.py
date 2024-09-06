def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            curr = str(num)
            if curr[0] in ('1', '3', '5', '7', '9') and curr[-1] in ('1', '3', '5', '7', '9'):
                oddCount += 1
    return oddCount