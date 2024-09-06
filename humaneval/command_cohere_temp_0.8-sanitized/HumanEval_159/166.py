def eat(n, need, rem):
    ct, leftovers = 0, 0
    while need:
        if need >= rem:
            ct += rem
            need -= rem
        else:
            ct += need
            leftovers += need - rem
        rem = max(0, rem - need)
    return [ct, leftovers]