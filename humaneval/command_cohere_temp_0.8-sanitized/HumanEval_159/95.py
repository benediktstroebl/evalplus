def eat(n, need, rem):
    cnt = max(0, min(need, rem))
    n += cnt
    rem -= cnt
    return [n, rem]