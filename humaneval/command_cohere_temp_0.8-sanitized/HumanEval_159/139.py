def eat(n, need, rem):
    ct, leftovers = 0, 0
    while need:
        if need > rem:
            leftovers = 0
            ct += rem
            need -= rem
        else:
            ct += need
            leftovers = rem - need
        rem = 0
    return [ct, leftovers]