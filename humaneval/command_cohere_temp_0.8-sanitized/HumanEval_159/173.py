def eat(n, need, rem):
    ct, leftover = 0, 0
    while need:
        if leftover == 0:
            return [n, leftover]
        ct += need
        leftover -= 1
        need -= 1
    while leftover > 0:
        ct += leftover
        leftover = 0
    return [ct, leftover]