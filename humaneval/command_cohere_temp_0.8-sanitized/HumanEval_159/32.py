def eat(n, need, rem):
    ate, leftovers = 0, 0
    while need > 0 and rem > 0:
        ate += min(need, rem)
        need -= ate
        rem -= 1
        leftovers += ate
    return [n + ate, leftovers]