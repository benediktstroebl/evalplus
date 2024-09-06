def eat(n, need, rem):
    ans = [n + need, min(need, rem)]
    if ans[1] == need:
        return ans
    else:
        return [ans[0], 0]