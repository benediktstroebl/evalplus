def eat(n, need, rem):
    guts, leave = 0, 0
    while need:
        if need >= rem:
            guts += rem
            leave = 0
            break
        else:
            guts += need
            leave = rem - need
            need = 0
    return [guts, leave]