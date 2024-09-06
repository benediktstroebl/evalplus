def eat(n, need, rem):
    n, need, rem = int(n), int(need), int(rem)
    eaten, leftover = n, rem
    if n + need > rem:
        eaten = rem
    elif n + need > leftover:
        eaten = leftover
    leftover = leftover - eaten
    return [eaten, leftover]