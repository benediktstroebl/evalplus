def eat(n, need, rem):
    ct = n + need
    rt = max(0, rem - (need))
    return [ct, rt]