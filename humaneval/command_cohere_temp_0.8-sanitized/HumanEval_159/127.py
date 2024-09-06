def eat(n, need, rem):
    ans = [n + need, min(rem, need)]
    if rem < need:
        ans[1] = 0
    return ans