def eat(n, need, rem):
    ct, leftover = 0, 0
    while need:
        if need >= rem:
            ct += rem
            need -= rem
        else:
            ct += need
            leftover += need - rem
        rem = 0
    return [ct, leftover]