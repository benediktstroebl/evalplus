def eat(n, need, rem):
    prey = n + need
    if prey > rem:
        full = rem
    else:
        full = prey
    return [full, rem - full]