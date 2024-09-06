def eat(n, need, rem):
    ate = n + min(need, rem)
    rem = max(0, rem - need)
    return [ate, rem]