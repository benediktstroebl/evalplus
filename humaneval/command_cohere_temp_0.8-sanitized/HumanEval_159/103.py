def eat(n, need, rem):
    ate, leftover = 0, 0
    while need > 0 and rem > 0:
        leftover += 1
        ate += min(need, rem)
        need -= ate
        rem -= 1
    return [n + ate, leftover]