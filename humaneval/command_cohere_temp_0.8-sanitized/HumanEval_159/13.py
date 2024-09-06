def eat(n, need, rem):
    ct = n + need
    rt = max(0, rem - ct)
    return [ct, rt]