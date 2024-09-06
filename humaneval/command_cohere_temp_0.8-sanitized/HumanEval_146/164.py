import unittest
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)