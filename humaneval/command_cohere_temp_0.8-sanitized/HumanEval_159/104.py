def eat(n, need, rem):
    ate = n
    if ate + need > rem:
        (ate) = rem
    print(f"ate={ate}, hunger={need-ate}, remaining={rem-ate}")
    return [ate, rem-ate]