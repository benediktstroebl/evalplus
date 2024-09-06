def eat(n, need, rem):
    ate = n
    if need > rem:
        ate = rem
    print(f"[{n}, {rem}]")
    return [n+ate, rem-ate]