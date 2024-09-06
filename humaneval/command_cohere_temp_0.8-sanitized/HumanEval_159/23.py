def eat(n, need, rem):
    ct, leave = 0, 0
    while need > 0:
        if need >= rem:
            ct += rem
            need -= rem
        else:
            ct += need
            leave += need
            need = 0
        rem -= min(rem, need)
    return [ct, leave]