def eat(n, need, rem):
    ate, leftover = n, rem
    if ate < need:
        ate += leftover
        leftover = 0
    return [ate, leftover]