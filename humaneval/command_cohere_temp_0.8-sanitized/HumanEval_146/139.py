def specialFilter(nums):
    oddFirst = lambda x: x[0] % 2 == 1 and x[1] % 2 == 1
    oddLast = lambda x: x[-1] % 2 == 1 and x[-2] % 2 == 1
    return sum(n for n in nums if oddFirst(n) and oddLast(n) and n > 10)