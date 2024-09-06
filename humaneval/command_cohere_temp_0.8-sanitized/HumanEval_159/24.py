def eat(n, need, rem):
    ct = n + need
    rt = rem >= ct
    if rt:
        return [ct, rem - ct]
    else:
        return [n + need, 0]