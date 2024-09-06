def specialFilter(nums):
    oddFirst = lambda x: (x / 10) % 2 == 1
    oddLast = lambda x: (x % 10) % 2 == 1
    return sum(x for x in nums if x > 10 and oddFirst(x) and oddLast(x))