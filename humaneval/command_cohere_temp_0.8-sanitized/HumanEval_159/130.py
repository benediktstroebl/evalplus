def eat(n, need, rem):
    ate = n
    if ate + need > rem:
        ate = rem
    print(f"Rabbit eats {ate} carrots, it remains with {rem-ate} carrots.")
    return [n+ate, rem-ate]