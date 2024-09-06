def eat(n, need, rem):
    ans = [n + need, max(0, rem - need)]
    return ans