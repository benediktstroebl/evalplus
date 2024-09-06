def specialFilter(nums):
    # Check if the list has only one element
    if len(nums) == 1:
        return 0
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)