def eat(n, need, rem):
    ans = [n + need, min(rem, need)]
    if ans[1] < need:
        ans[0] = ans[0] + (need - ans[1])
    return ans